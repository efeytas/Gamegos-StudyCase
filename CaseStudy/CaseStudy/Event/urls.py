from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    path('join/', views.join_event, name='list_event'),
]

        