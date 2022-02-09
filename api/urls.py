from django.urls import path
from api.views import HealthCheckApiView


urlpatterns = [
    path('health_check', HealthCheckApiView.as_view()),
]
