from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from api.serializers import AtmSerializer, AccountSerializer, BalanceSerializer
from api.models import Account
from atmauth.utils import ExpiringTokenAuthentication


class HealthCheckApiView(APIView):

    def get(self, request):
        return Response('Healthy')


class AccountListApiView(APIView):

    authentication_classes = (ExpiringTokenAuthentication,)

    def get(self, request):
        user = request.user
        user_accounts = user.account_set.all()
        return Response({'accounts': user_accounts.values_list('account_num', flat=True)})


class AccountGetApiView(APIView):

    authentication_classes = (ExpiringTokenAuthentication,)

    def get(self, request, account_num):
        user = request.user
        account = Account.objects.filter(
            user=user,
            account_num=account_num
        ).first()

        if not account:
            return Response(
                f"Given account number ({account_num}) for this user does not exist.",
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AccountSerializer(account)
        return Response(serializer.data)

#
# class DepositWithdrawApiView(APIView):
#
#     authentication_classes = (ExpiringTokenAuthentication,)
#     serializer_class = BalanceSerializer
#
#     def post(self, request, user_id):
#         serializer = self.serializer_class(data=request.data)
#
#         if serializer.is_valid():
#             url = request.get_full_path()
#             account_num = serializer.validated_data.get('account_num')
#             amount = serializer.validated_data.get('amount')
#
#             account = Account.objects.filter(
#                 user__id=user_id,
#                 account_num=account_num
#             ).first()
#             if not account:
#                 return Response(
#                     f"Given account number ({account_num}) does not exist.",
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
#     def _can_withdraw_from_bin(self, amount: int) -> bool:
#         # TODO: check if the cash bin has enough cash to withdraw
#         return True
#
#     def _deposit_bin(self, amount: int) -> bool:
#         # TODO: send call to cash bin to deposit and return if it was successful
#         return True
#
#     def _withdraw_bin(self, amount) -> bool:
#         # TODO: send call to cash bin to withdraw and return if it was successful
#         return True
