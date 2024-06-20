from django.shortcuts import render
from .schedule_generator import generate_schedule

# Create your views here.


def list_games(request):
    players = ["Debbie", "Cindy", "Carter", "Linda",
               "Burg", "Lauren", "Leo", "Rob"]
    courts = 2
    sched = list(generate_schedule(courts, players))
    for rounds in sched:
        for game in rounds:
            print('game', game)
        print(rounds)

    enumerated_schedule = enumerate(sched, start=1)
    context = {"schedule": enumerated_schedule}
    return render(request, 'schedule/list_games.html', context)
