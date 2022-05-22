from rest_framework import serializers
from .models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True,write_only=True)
    class Meta:
        model = User
        fields = ('username','phone_number','password','password2')
        

    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("password dosn't Match")
        return data


    def create(self, validated_data):
        del validated_data['password2']
        
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user       



class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)