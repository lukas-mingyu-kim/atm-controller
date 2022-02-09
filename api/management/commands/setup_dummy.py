
import calendar
import datetime
import logging
from django.core.management.base import BaseCommand
from django.db import transaction
from random import randint
from typing import List

from atmauth.models import AtmUser
from api.models import Account

NUM_USERS = 10
NUM_ACCOUNTS_PER_USER = 5


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            help='Number of dummy users to create',
        )
        parser.add_argument(
            '--accounts',
            type=int,
            help='Number of dummy accounts to create per user',
        )

    @transaction.atomic
    def handle(self, *args, **kwargs):
        num_users = kwargs.get('users') or NUM_USERS
        num_accounts = kwargs.get('accounts') or NUM_ACCOUNTS_PER_USER

        users = self.create_dummy_users(num_users)
        self.create_dummy_accounts(users, num_accounts)
        logging.info(f'{num_users} Users & {num_accounts} Accounts per user created.')

    def create_dummy_users(self, num_users: int) -> List[AtmUser]:
        AtmUser.objects.all().delete()
        users = []
        for i in range(num_users):
            user_index = i + 1
            user = AtmUser(
                id=user_index,
                card_num='1111222233334444' if i == 0 else str(randint(10 ** 15, 10 ** 16 - 1))
            )
            users.append(user)
        AtmUser.objects.bulk_create(users)
        return users

    def create_dummy_accounts(self, users: List[AtmUser], num_accounts: int) -> List[Account]:
        Account.objects.all().delete()
        accounts = []
        for user in users:
            for i in range(num_accounts):
                account = Account(
                    user=user,
                    account_num=str(randint(10 ** 19, 10 ** 20 - 1)),
                    balance=randint(50, 10 ** 5),
                )
                accounts.append(account)

        Account.objects.bulk_create(accounts)
        return accounts
