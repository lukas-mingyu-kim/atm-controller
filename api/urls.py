from django.urls import path
from api.views import HealthCheckApiView, AccountApiView


urlpatterns = [
    path('health_check', HealthCheckApiView.as_view()),
    path('accounts', AccountApiView.as_view()),
]
