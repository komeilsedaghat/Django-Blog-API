from django.shortcuts import render
from rest_framework import views
from rest_framework import generics
from django.contrib.auth import authenticate,login
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserRegisterSerializer,ChangePasswordSerializer,AdminPanelSerializer
from rest_framework.throttling import UserRateThrottle
from .throttle import CustomUserRegiserThrottle
from rest_framework.permissions import IsAuthenticated
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from .permissions import IsSuperUser
from rest_framework.pagination import LimitOffsetPagination
from django.http import Http404

# Create your views here.

class RegisterUserView(generics.CreateAPIView):
    throttle_classes = (CustomUserRegiserThrottle,)
    serializer_class = UserRegisterSerializer


#change Password
class ChangePasswordView(generics.UpdateAPIView):
    throttle_classes = (UserRateThrottle,)
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)
    def get_object(self):
        user = self.request.user
        return user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get('old_password')):
                return Response({'Error':'Your Old Password Is Wrong!'},status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'Done':'Your Password Changed Successfuly'},status=status.HTTP_200_OK)




@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        "Password Reset",
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )




class AdminPanelView(views.APIView,LimitOffsetPagination):
    permission_classes = (IsSuperUser,)

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        user = User.objects.all()
        serializer = AdminPanelSerializer(user, many=True)

        results = self.paginate_queryset(user, request, view=self)
        serializer = AdminPanelSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)


    def post(self,request):
        serializer = AdminPanelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        user = self.get_object(pk)
        serializer = AdminPanelSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class RevokeTokenView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self,request):
        request.auth.delete()
        return Response({'msg':'Your Toekn Revoked!'})
