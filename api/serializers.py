
from rest_framework import serializers

from api.models import Account


class DepositWithdrawSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=0)


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('account_num', 'user', 'balance')
        # extra_kwargs = {'user': {'read_only': True}}
