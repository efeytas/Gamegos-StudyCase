from .models import Player
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

# serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(False)
    class Meta:
        model = Player
        fields = ('level', 'created_at', 'user')


    

    



    

    

