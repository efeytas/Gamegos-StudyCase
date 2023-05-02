from django.db import models
from CaseStudy.Player.models import Player
from enum import Enum

# constants
BRONZE_MIN_LEVEL = 1
BRONZE_MAX_LEVEL = 20
SILVER_MIN_LEVEL = 21
SILVER_MAX_LEVEL = 49
GOLD_MIN_LEVEL = 50
MAX_PLAYER_PER_GROUP = 20

# enums
class Category(models.TextChoices):
    GOLD = 'GOLD', 'Gold'
    SILVER = 'SILVER', 'Silver'
    BRONZE = 'BRONZE', 'Bronze'

class Event(models.Model):
    def __str__(self):
        return str(self.id)

# group model
class Group(models.Model):
    event = models.ForeignKey(
        Event, 
        on_delete=models.CASCADE
    )
    members = models.ManyToManyField(
        Player,
        through='Membership',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=6,
        choices=Category.choices,
    )

# membership model
class Membership(models.Model):
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE
    )
    player = models.ForeignKey(
        Player, 
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)


    


        



