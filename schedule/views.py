from django.shortcuts import render, get_object_or_404, redirect
from .schedule_generator import generate_round
from players_lists.models import PlayersList
from django.contrib.auth.decorators import login_required


def get_next_round(courts, players, games_counter, team_history):
    result = generate_round(courts, players, games_counter, team_history)

  # Process the schedule to match template expectations
    if result:
        round_games, sitting_out, games_counter, team_history = result
        processed_round = []
        for game in round_games:
            processed_game = {
                "team1_player1": game.team1[0],
                "team1_player2": game.team1[1],
                "team2_player1": game.team2[0],
                "team2_player2": game.team2[1]
            }

            processed_round.append(processed_game)
        return {"games": processed_round, "sitting_out": sitting_out}, games_counter, team_history

    return None


def clear_session(request, players, id, courts):
    request.session["games_counter"] = {
        player: 0 for player in players}
    request.session["team_history"] = []
    request.session["rounds"] = []
    request.session["num_courts"] = courts
    return redirect('list_games', id=id)


@login_required
def list_games(request, id):
    players_list = get_object_or_404(PlayersList, id=id)
    title = players_list.title
    players = [player.name for player in players_list.players.all()]
    max_attempts = 1000

    if request.method == "POST":
        if "create_schedule" in request.POST:
            num_courts = request.POST.get('num_courts')
            courts = int(num_courts)
            # Clear session data for a new schedule
            request.session["games_counter"] = {
                player: 0 for player in players}
            request.session["team_history"] = []
            request.session['num_rounds_played'] = 0
            request.session["rounds"] = []
            request.session["num_courts"] = courts
            request.session['extra_rounds'] = False
            return redirect('list_games', id=id)

    games_counter = request.session["games_counter"]
    team_history = request.session["team_history"]
    num_courts = request.session["num_courts"]
    num_rounds_played = request.session["num_rounds_played"]

    if min(games_counter.values()) < len(players)-1:
        for counter in range(max_attempts):

            result = get_next_round(
                num_courts, players, games_counter, team_history)

            if result:
                next_round, games_counter, team_history = result
                break

        if not result:
            request.session["team_history"] = []
            team_history = request.session["team_history"]
            result = get_next_round(
                num_courts, players, games_counter, team_history)
            if result:
                next_round, games_counter, team_history = result

        if result:
            num_rounds_played += 1
            request.session["games_counter"] = games_counter
            request.session["team_history"] = team_history
            request.session["rounds"].append(next_round)
            request.session["num_rounds_played"] = num_rounds_played
    elif min(games_counter.values()) == len(players)-1 and not request.session["extra_rounds"]:
        set_rounds = list(request.session["rounds"])
        request.session['set_rounds'] = set_rounds
        num_rounds_played = request.session["num_rounds_played"]
        appended_round = num_rounds_played % len(set_rounds)
        request.session["rounds"].append(set_rounds[appended_round])
        num_rounds_played += 1
        request.session["num_rounds_played"] = num_rounds_played
        request.session["extra_rounds"] = True

    else:
        num_rounds_played = request.session["num_rounds_played"]
        set_rounds = request.session['set_rounds']
        appended_round = num_rounds_played % len(set_rounds)
        request.session["rounds"].append(set_rounds[appended_round])
        num_rounds_played += 1
        request.session["num_rounds_played"] = num_rounds_played

    rounds_with_numbers = [{"round_number": num_rounds_played-i, "round": round}
                           for i, round in enumerate(reversed(request.session["rounds"]))]

    context = {
        "schedule": rounds_with_numbers,
        "list_title": title,
        "num_courts": num_courts,
        "list_id": id
    }
    return render(request, 'schedule/list_games.html', context)
