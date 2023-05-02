from django.db import models
from CaseStudy.Player.models import Player
from enum import Enum


class Category(models.TextChoices):
    GOLD = 'GOLD', 'Gold'
    SILVER = 'SILVER', 'Silver'
    BRONZE = 'BRONZE', 'Bronze'

class Event(models.Model):
    def __str__(self):
        return str(self.id)

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


    


        



# Create your models here.
