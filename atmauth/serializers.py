from rest_framework import serializers


class SigninSerializer(serializers.Serializer):
    card_num = serializers.CharField(max_length=20)
    pin_num = serializers.CharField(max_length=6)
