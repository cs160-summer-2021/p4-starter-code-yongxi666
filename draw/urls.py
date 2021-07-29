# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('kiosk/', views.kiosk, name='kiosk'),
    path('<str:room_name>/', views.room, name='room'),

]
