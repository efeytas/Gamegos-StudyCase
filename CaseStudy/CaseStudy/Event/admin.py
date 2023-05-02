from django.contrib import admin
from .models import Event, Group, Membership

admin.site.register(Event)
admin.site.register(Group)
admin.site.register(Membership)


# Register your models here.
