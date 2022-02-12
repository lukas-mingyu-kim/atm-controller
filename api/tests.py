from django.test import TestCase
from rest_framework.response import Response

from api.models import Account
from atmauth.models import AtmUser
from atmauth.tests import TEST_CARD_NUM

TEST_ACCOUNT_NUM1 = 'TEST_ACCOUNT_NUM1'  # Use to test deposit
TEST_ACCOUNT_NUM2 = 'TEST_ACCOUNT_NUM2'  # Use to test withdraw
TEST_DEFAULT_BALANCE = 10000


class SampleApiTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = AtmUser.objects.create_user(
            card_num=TEST_CARD_NUM,
            password='123456',
        )
        user.save()

        accounts = []
        for account_num in [TEST_ACCOUNT_NUM1, TEST_ACCOUNT_NUM2]:
            account = Account(
                user=user,
                account_num=account_num,
                balance=TEST_DEFAULT_BALANCE,
            )
            accounts.append(account)
        Account.objects.bulk_create(accounts)

    def test_list_accounts(self):
        _, token = self._signin(TEST_CARD_NUM)
        account_response = self.client.get(
            '/api/accounts',
            **{'HTTP_AUTHORIZATION': f'Token {token}'},
        )

        self.assertEquals(account_response.status_code, 200)
        response_body = account_response.data
        self.assertTrue('accounts' in response_body)
        self.assertEquals(len(response_body['accounts']), 2)
        self.assertEquals(set(response_body['accounts']), {TEST_ACCOUNT_NUM1, TEST_ACCOUNT_NUM2})

    def test_get_account(self):
        user_id, token = self._signin(TEST_CARD_NUM)
        account_response = self.client.get(
            f'/api/accounts/{TEST_ACCOUNT_NUM1}',
            **{'HTTP_AUTHORIZATION': f'Token {token}'},
        )
        self._check_account_response(account_response, user_id, TEST_DEFAULT_BALANCE)

    def test_get_account_wrong_token(self):
        user_id, token = self._signin(TEST_CARD_NUM)
        account_response = self.client.get(
            f'/api/accounts/{TEST_ACCOUNT_NUM1}',
            **{'HTTP_AUTHORIZATION': f'Token {token[:-1]}'},
        )
        self.assertEquals(account_response.status_code, 401)
        self.assertEquals(str(account_response.data['detail']), 'Invalid token')

    def test_get_wrong_account(self):
        wrong_account_num = 'WRONG_ACCOUNT_NUM'
        user_id, token = self._signin(TEST_CARD_NUM)
        account_response = self.client.get(
            f'/api/accounts/{wrong_account_num}',
            **{'HTTP_AUTHORIZATION': f'Token {token}'},
        )
        self.assertEquals(account_response.status_code, 404)
        self.assertEquals(account_response.data['detail'],
                          f'Given account number ({wrong_account_num}) for this user does not exist.')

    def test_deposit(self):
        user_id, token = self._signin(TEST_CARD_NUM)
        deposit_amount = 1000
        deposit_response = self.client.patch(
            f'/api/accounts/{TEST_ACCOUNT_NUM1}/deposit',
            data={
                'amount': deposit_amount,
            },
            content_type="application/json",
            **{'HTTP_AUTHORIZATION': f'Token {token}'},
        )
        self._check_account_response(deposit_response, user_id, TEST_DEFAULT_BALANCE + deposit_amount)

    def test_withdraw(self):
        user_id, token = self._signin(TEST_CARD_NUM)
        withdraw_amount = 1000
        withdraw_response = self.client.patch(
            f'/api/accounts/{TEST_ACCOUNT_NUM2}/withdraw',
            data={
                'amount': withdraw_amount,
            },
            content_type="application/json",
            **{'HTTP_AUTHORIZATION': f'Token {token}'},
        )
        self._check_account_response(withdraw_response, user_id, TEST_DEFAULT_BALANCE - withdraw_amount)

    def test_withdraw_fail(self):
        user_id, token = self._signin(TEST_CARD_NUM)
        withdraw_amount = TEST_DEFAULT_BALANCE * 2
        withdraw_response = self.client.patch(
            f'/api/accounts/{TEST_ACCOUNT_NUM2}/withdraw',
            data={
                'amount': withdraw_amount,
            },
            content_type="application/json",
            **{'HTTP_AUTHORIZATION': f'Token {token}'},
        )
        self.assertEquals(withdraw_response.status_code, 422)
        self.assertEquals(withdraw_response.data['detail'], 'Balance not sufficient.')

        account_response = self.client.get(
            f'/api/accounts/{TEST_ACCOUNT_NUM2}',
            **{'HTTP_AUTHORIZATION': f'Token {token}'}
        )
        self._check_account_response(account_response, user_id, TEST_DEFAULT_BALANCE)

    def _signin(self, card_num: str, pin_num: str = '123456') -> (int, str):
        signin_response = self.client.post(
            '/auth/signin',
            data={
                'card_num': card_num,
                'pin_num': pin_num,
            },
        )
        return signin_response.data['user_id'], signin_response.data['token']

    def _check_account_response(self, response: Response, user_id: int, expected_balance: int):
        self.assertEquals(response.status_code, 200)
        response_body = response.data
        self.assertTrue('account_num' in response_body)
        self.assertTrue('user' in response_body)
        self.assertEquals(response_body['user'], user_id)
        self.assertTrue('balance' in response_body)
        self.assertEquals(response_body['balance'], expected_balance)

