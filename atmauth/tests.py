from django.test import TestCase

TEST_CARD_NUM = '1234123412341234'


class SampleApiTests(TestCase):

    def test_login(self):
        response = self.client.post(
            '/auth/signin',
            data={
                'card_num': TEST_CARD_NUM,
                'pin_num': '123456',
            },
        )
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'user_id')
        self.assertContains(response, 'token')
