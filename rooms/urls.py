from django.urls import path

from rooms.views import rooms, rooms_detail

urlpatterns = [
    path('', rooms, name='rooms'),
    path('<slug:slug>/', rooms_detail, name='rooms_detail'),
]