from django.shortcuts import render, get_object_or_404
from .schedule_generator import generate_schedule
from players_lists.models import PlayersList
from django.contrib.auth.decorators import login_required


def get_schedule(courts, players):
    schedule = generate_schedule(courts, players)

  # Process the schedule to match template expectations
    processed_schedule = []
    for round_games in schedule:
        processed_round = []

        sitting_out = round_games.pop()  # The last item is the sitting out players
        for game in round_games:
            processed_game = {
                "team1_player1": game.team1[0],
                "team1_player2": game.team1[1],
                "team2_player1": game.team2[0],
                "team2_player2": game.team2[1]
            }

            processed_round.append(processed_game)
        processed_schedule.append({
            "games": processed_round,
            "sitting_out": sitting_out
        })
    return processed_schedule


@login_required
def list_games(request, id):
    players_list = get_object_or_404(PlayersList, id=id)
    num_courts = request.POST.get('num_courts')
    title = players_list.title

    players = [player.name for player in players_list.players.all()]
    courts = int(num_courts)

    schedule = get_schedule(courts, players)

    context = {
        "schedule": schedule,
        "list_title": title,
        "num_courts": courts,
        "list_id": id
    }
    return render(request, 'schedule/list_games.html', context)


@login_required
def regenerate_schedule(request, id, num_courts):
    players_list = get_object_or_404(PlayersList, id=id)
    title = players_list.title
    players = [player.name for player in players_list.players.all()]
    schedule = get_schedule(num_courts, players)

    context = {
        "schedule": schedule,
        "list_title": title,
        "num_courts": num_courts,
        "list_id": id
    }
    return render(request, 'schedule/list_games.html', context)
