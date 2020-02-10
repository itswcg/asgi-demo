from django.http import HttpResponse
from django.shortcuts import render


def http(request):
    return HttpResponse("Hello, world")


def index(request):
    return render(request, 'demo/chat.html', {})


def room(request, room_name):
    return render(request, 'demo/room.html', {
        'room_name': room_name
    })
