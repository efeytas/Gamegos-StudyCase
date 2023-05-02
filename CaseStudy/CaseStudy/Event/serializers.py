from .models import Event, Group, Membership
from rest_framework import serializers
from CaseStudy.Player.serializers import PlayerSerializer, UserSerializer
from CaseStudy.Player.models import Player
from rest_framework.response import Response

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields= "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','members', 'created_at', 'category')


class MembershipSerializer(serializers.ModelSerializer):
    player = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()
    class Meta:
        model = Membership
        fields = ('id', 'group', 'player', 'event', 'created_at')
    
    def get_player(self, obj):
        player = Player.objects.get(id=obj.player.id)
        serializer = PlayerSerializer(player)
        return serializer.data
    
    def get_event(self, obj):
        event = Event.objects.get(id=obj.event.id)
        serializer = EventSerializer(event)
        return serializer.data