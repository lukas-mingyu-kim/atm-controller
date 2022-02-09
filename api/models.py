from django.db import models
from django.conf import settings


class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    account_num = models.CharField(max_length=20, unique=True)
    balance = models.IntegerField(default=0)
