from rest_framework import viewsets
from .models import Player
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
def get_user_profile(user):
    return get_object_or_404(Player, user=user)

class UserMixin:
    @action(detail=False, 
            methods=['POST'],
            url_path='register',
            url_name='register',
            )
    def register(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            user = User.objects.create_user(
                username=request.data['username'],
            )
            user.set_password(request.data['password'])
            user.save()
            player = Player(
                user = User.objects.get(username=request.data['username']),
                level = 1
            )
            player.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    @action(detail=False,
            methods=['POST'],
            url_path='levelup',
            url_name='levelup',
            )
    def levelup(self, request, *args, **kwargs):
        player = get_user_profile(request.user)
        player.level += 1
        player.save()
        return Response("User " + player.user.username +" Level Up to " + str(player.level) + " !")
        
    

class PlayerViewSet(viewsets.ModelViewSet,
                   UserMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        if self.action == 'register':
            return []
        else:
            return [IsAuthenticated()]
        


    def create(self, request, *args, **kwargs):
        return self.register(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return self.levelup(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return Response(User.objects.values_list('username', flat=True))

        



        
    



        
    