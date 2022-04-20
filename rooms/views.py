from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rooms.models import Room, Message


@login_required
def rooms(request):
    rooms = Room.objects.all()
    ctx = {
        'rooms': rooms
    }
    return render(request, 'rooms/rooms.html', ctx)


@login_required
def rooms_detail(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    ctx = {
        'room': room,
        'messages': messages,
    }
    return render(request, 'rooms/rooms_detail.html', ctx)
