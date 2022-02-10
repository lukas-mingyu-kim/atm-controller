from django.urls import path
from api.views import HealthCheckApiView, AccountListApiView, AccountGetApiView


urlpatterns = [
    path('health_check', HealthCheckApiView.as_view()),
    path('accounts', AccountListApiView.as_view()),
    path('accounts/<str:account_num>', AccountGetApiView.as_view()),
]
