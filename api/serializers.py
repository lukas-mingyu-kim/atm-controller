
from rest_framework import serializers

from api.models import Account


class AtmSerializer(serializers.Serializer):
    card_num = serializers.CharField(max_length=20)


class BalanceSerializer(serializers.Serializer):
    account_num = serializers.CharField(max_length=20)
    amount = serializers.IntegerField()


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('account_num', 'user', 'balance')
        extra_kwargs = {'user': {'read_only': True}}
