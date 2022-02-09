from django.urls import path

from atmauth import views


urlpatterns = [
    path('signin', views.SigninApiView.as_view()),
]