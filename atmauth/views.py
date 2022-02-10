from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from atmauth.serializers import SigninSerializer
from atmauth.models import AtmUser
from atmauth.utils import is_token_expired


class SigninApiView(ObtainAuthToken):

    serializer_class = SigninSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            card_num = serializer.validated_data.get('card_num')
            pin_num = serializer.validated_data.get('pin_num')
            if not self._is_pin_valid(card_num, pin_num):
                return Response(status=status.HTTP_401_UNAUTHORIZED)

            if not AtmUser.objects.filter(card_num=card_num).exists():
                user = AtmUser.objects.create_user(
                    card_num=card_num, password=pin_num)
                user.save()
            else:
                user = AtmUser.objects.get(card_num=card_num)

            token, created = Token.objects.get_or_create(user=user)
            if is_token_expired(token):
                token.delete()
                token = Token.objects.create(user=token.user)

            return Response({
                'user_id': user.id,
                'token': token.key
            })

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def _is_pin_valid(self, card_num: str, pin_num: str) -> bool:
        # TODO: call bank API to check the PIN
        return True
