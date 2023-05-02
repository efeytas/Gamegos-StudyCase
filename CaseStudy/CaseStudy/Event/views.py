from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Event, Group, Membership, Category, BRONZE_MIN_LEVEL, BRONZE_MAX_LEVEL, SILVER_MIN_LEVEL, SILVER_MAX_LEVEL, GOLD_MIN_LEVEL, MAX_PLAYER_PER_GROUP
from CaseStudy.Player.models import Player
from .serializers import EventSerializer, GroupSerializer, MembershipSerializer
from django.shortcuts import get_object_or_404
from django.db import transaction



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


# using transaction atomic for concurrency this decorator will lock the database until the function is done
@transaction.atomic
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_event(request):
    # get the player
    player = get_user_profile(request.user)
    event = Event.objects.get(id=request.data['event_id'])
    if  BRONZE_MIN_LEVEL <= player.level <= BRONZE_MAX_LEVEL:
        #use select_for_update() to lock the database
        group = Group.objects.filter(event=event,category=Category.BRONZE).select_for_update().last()
        # if there is no group create one
        if(group == None):
            group = Group(
                event = event,
                category = Category.BRONZE,
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
            # if there is a group check if the player already joined
            if(Membership.objects.filter(group=group,player=player).count() > 0):
                group.save()
                return Response("You already joined this event")
            # if the group is not full add the player to the group
            if(group.members.count() < MAX_PLAYER_PER_GROUP ):
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                group.save()
                membership.save()
                return Response(GroupSerializer(group).data)
            # if the group is full create a new group
            elif(group.members.count() == MAX_PLAYER_PER_GROUP):
                group.save()
                group = Group(
                    event = event,
                    category = Category.BRONZE
                )
                group.save()
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                membership.save()
                return Response(GroupSerializer(group).data)
    # same logic for silver and gold
    elif SILVER_MIN_LEVEL < player.level < SILVER_MAX_LEVEL:
        group = Group.objects.filter(event=event,category=Category.SILVER).select_for_update().last()
        if(group == None):
            group = Group(
                event = event,
                category = Category.SILVER
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
                group.save()
                return Response("You already joined this event")
            if(group.members.count() < MAX_PLAYER_PER_GROUP ):
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                group.save()
                membership.save()
                return Response(GroupSerializer(group).data)
            elif(group.members.count() == 20):
                group.save()
                group = Group(
                    event = event,
                    category = Category.SILVER
                )
                group.save()
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                membership.save()
                return Response(GroupSerializer(group).data)    
    elif GOLD_MIN_LEVEL <= player.level:
        group = Group.objects.filter(event=event,category=Category.GOLD).select_for_update().last()
        if(group == None):
            group = Group(
                event = event,
                category = Category.GOLD
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
                group.save()
                return Response("You already joined this event")
            if(group.members.count() < MAX_PLAYER_PER_GROUP ):
                group.save()
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                membership.save()
                return Response(GroupSerializer(group).data)
            elif(group.members.count() == MAX_PLAYER_PER_GROUP):
                group.save()
                group = Group(
                    event = event,
                    category = Category.GOLD
                )
                group.save()
                membership = Membership(
                    group = group,
                    player = player,
                    event = event
                )
                membership.save()
                return Response(GroupSerializer(group).data) 
    # if the player level is not in the range of the event level return error
    else:
        player.level = 1
        player.save()
        return Response("Invalid Level Your Level Setted to 1")

   



    

        
        



        
    


