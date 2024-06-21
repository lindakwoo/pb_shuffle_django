from django.contrib import admin
from .models import PlayersList, Player

# Register your models here.


@admin.register(PlayersList)
class PlayersListAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'owner'
    ]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'player_list_title',
        'owner'
    ]
