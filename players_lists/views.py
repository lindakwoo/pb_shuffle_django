from django.shortcuts import render, redirect, get_object_or_404
from .models import PlayersList, Player
from players_lists.forms import PlayersListForm

# Create your views here.


def players_lists(request):
    players_lists = PlayersList.objects.all()
    context = {'lists': players_lists}
    return render(request, 'players_lists/players_lists.html', context)


def players_list_create(request):
    if request.method == "POST":
        form = PlayersListForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            names = request.POST.getlist('new_players')
            players_list = PlayersList.objects.create(
                title=title, owner=request.user)
            for name in names:
                if name:
                    Player.objects.create(
                        name=name, owner=request.user,
                        player_list=players_list)

                # redirect to the list detail page
            return redirect('home')
    else:
        form = PlayersListForm()
        context = {
            'form': form,

        }
        return render(request, 'players_lists/create_players_list.html',
                      context)


def players_list_detail(request, id):
    list = get_object_or_404(PlayersList, id=id)
    context = {'list': list}
    return render(request, 'players_lists/players_list_detail.html', context)


def delete_player(request, list_id, player_id,):
    player = get_object_or_404(Player, id=player_id)
    player.delete()
    return redirect("players_list_detail", id=list_id)


def save_player(request, id, player_name):
    list = get_object_or_404(PlayersList, id=id)
    Player.objects.create(
        name=player_name, owner=request.user, player_list=list)

    return redirect("players_list_detail", id=id)
