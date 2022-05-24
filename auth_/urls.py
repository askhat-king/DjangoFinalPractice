from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from .views import UserRegisterView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', UserRegisterView.as_view(), name='register')
]
