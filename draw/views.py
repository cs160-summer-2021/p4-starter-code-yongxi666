# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

def home(request):
    return render(request, 'draw/home.html')

def users(request):
    return render(request, 'draw/users.html')

def kiosk(request):
    return render(request, 'draw/kiosk.html')