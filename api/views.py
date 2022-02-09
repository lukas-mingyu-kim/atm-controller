from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import AtmSerializer, AccountSerializer
from atmauth.utils import ExpiringTokenAuthentication


class HealthCheckApiView(APIView):

    def get(self, request):
        return Response('Healthy')


class AccountApiView(APIView):

    authentication_classes = (ExpiringTokenAuthentication,)
    serializer_class = AtmSerializer

    def get(self, request):
        user = request.user
        user_accounts = user.account_set.all()
        serializer = AccountSerializer(user_accounts, many=True)
        return Response({'accounts': serializer.data})

#
# class DepositWithdrawApiView(APIView):
#
#     authentication_classes = (ExpiringTokenAuthentication,)
#     permission_classes = (permissions.OwnAccount,)
#     serializer_class = serializers.BalanceSerializer
#
#     def post(self, request, user_id):
#         serializer = self.serializer_class(data=request.data)
#
#         if serializer.is_valid():
#             url = request.get_full_path()
#             account_num = serializer.validated_data.get('account_num')
#             amount = serializer.validated_data.get('amount')
#
#             account = models.Account.objects.filter(user__id=user_id, account_num=account_num).first()
#             if not account:
#                 return Response(
#                     "No such account",
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
#
#             with transaction.atomic():
#                 if url.endswith('deposit'):
#                     self._deposit_bin(amount)
#                     account.balance += amount
#                     account.save()
#                 else:
#                     if account.balance - amount < 0:
#                         return Response(
#                             "Balance not sufficient",
#                             status=status.HTTP_400_BAD_REQUEST
#                         )
#
#                     self._withdraw_bin(amount)
#                     account.balance -= amount
#                     account.save()
#
#             serializer = serializers.AccountSerializer(account)
#             return Response({'account': serializer.data})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#     def _can_withdraw_from_bin(self, amount):
#         # TODO: check cash bin for enough cash to withdraw
#         return True
#
#     def _deposit_bin(self, amount):
#         # TODO: send call to cash bin to deposit
#         return
#
#     def _withdraw_bin(self, amount):
#         # TODO: send call to cash bin to deposit
#         return