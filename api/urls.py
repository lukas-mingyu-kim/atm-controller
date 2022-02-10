from django.urls import path
from api.views import HealthCheckApiView, AccountListApiView, AccountGetApiView, DepositWithdrawApiView


urlpatterns = [
    path('health_check', HealthCheckApiView.as_view()),
    path('accounts', AccountListApiView.as_view()),
    path('accounts/<str:account_num>', AccountGetApiView.as_view()),
    path('accounts/<str:account_num>/deposit', DepositWithdrawApiView.as_view(), name='deposit'),
    path('accounts/<str:account_num>/withdraw', DepositWithdrawApiView.as_view(), name='withdraw'),
]
