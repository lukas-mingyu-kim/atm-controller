from django.urls import path

from atmauth.views import SigninApiView


urlpatterns = [
    path('signin', SigninApiView.as_view()),
]
