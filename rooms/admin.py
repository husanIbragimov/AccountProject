from django.contrib import admin

from .models import Room, Message


class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Room, RoomAdmin)
admin.site.register(Message)
