from django.shortcuts import render, get_object_or_404
from .schedule_generator import generate_schedule
from players_lists.models import PlayersList

# Create your views here.


def list_games(request, id):
    players_list = get_object_or_404(PlayersList, id=id)
    title = players_list.title

    def get_player_names(players_list):
        player_names = [
            player.name for player in players_list.players.all()]
        return player_names
    players = get_player_names(players_list)
    print(players)
    courts = 2
    sched = list(generate_schedule(courts, players))
    context = {"schedule": sched, "list_title": title}
    return render(request, 'schedule/list_games.html', context)
