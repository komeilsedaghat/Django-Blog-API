from django.shortcuts import render
from rest_framework import views
from rest_framework import generics
from django.contrib.auth import authenticate,login
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserRegisterSerializer
# Create your views here.

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


