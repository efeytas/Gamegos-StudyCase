from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Event, Group, Membership
from CaseStudy.Player.models import Player
from .serializers import EventSerializer, GroupSerializer, MembershipSerializer
from django.shortcuts import get_object_or_404


def get_user_profile(user):
    return get_object_or_404(Player, user=user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Event Created")
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_event(request):
    player = get_user_profile(request.user)
    event = Event.objects.get(id=request.data['event_id'])
    if   1 <= player.level <= 20:
        group = Group.objects.filter(event=event,category="BRONZE").last()
        if(group == None):
            group = Group(
                event = event,
                category = "BRONZE"
            )
            group.save()
            membership = Membership(
                group = group,
                player = player,
                event = event
            )
            membership.save()
            return Response(GroupSerializer(group).data)
        else:
            if(Membership.objects.filter(group=group,player=player).count() > 0):
                return Response("You already joined this event")
            if(group.members.count() < 20 ):
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                membership.save()
                return Response(GroupSerializer(group).data)
            elif(group.members.count() == 20):
                group = Group(
                    event = event,
                    category = "BRONZE"
                )
                group.save()
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                membership.save()
                return Response(GroupSerializer(group).data)
    elif 20 < player.level < 49:
        group = Group.objects.filter(event=event,category="SILVER").last()
        if(group == None):
            group = Group(
                event = event,
                category = "SILVER"
            )
            group.save()
            membership = Membership(
                group = group,
                player = player,
                event = event
            )
            membership.save()
            return Response(GroupSerializer(group).data)
        else:
            if(Membership.objects.filter(group=group,player=player).count() > 0):
                return Response("You already joined this event")
            if(group.members.count() < 20 ):
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                membership.save()
                return Response(GroupSerializer(group).data)
            elif(group.members.count() == 20):
                group = Group(
                    event = event,
                    category = "SILVER"
                )
                group.save()
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                membership.save()
                return Response(GroupSerializer(group).data)    
    elif 50 <= player.level:
        group = Group.objects.filter(event=event,category="GOLD").last()
        if(group == None):
            group = Group(
                event = event,
                category = "GOLD"
            )
            group.save()
            membership = Membership(
                group = group,
                player = player,
                event = event
            )
            membership.save()
            return Response(GroupSerializer(group).data)
        else:
            if(Membership.objects.filter(group=group,player=player).count() > 0):
                return Response("You already joined this event")
            if(group.members.count() < 20 ):
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                membership.save()
                return Response(GroupSerializer(group).data)
            elif(group.members.count() == 20):
                group = Group(
                    event = event,
                    category = "GOLD"
                )
                group.save()
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                membership.save()
                return Response(GroupSerializer(group).data)    



    

        
        



        
    


