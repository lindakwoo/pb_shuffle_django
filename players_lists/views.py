from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import PlayersList, Player
from players_lists.forms import PlayersListForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods
import json
from django.contrib.auth.models import User


class PlayerListEncoder(ModelEncoder):
    model = PlayersList
    properties = ["title", "id"]


def home_page(request):
    has_lists = False
    if request.user.is_authenticated:
        players_lists = PlayersList.objects.filter(owner=request.user)
        if players_lists:
            has_lists = True
    context = {"has_lists": has_lists}

    return render(request, 'players_lists/home.html', context)


@require_http_methods(["GET", "POST"])
# @login_required
def players_lists(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("user")
        user = get_object_or_404(User, username=username)
        players_lists = PlayersList.objects.filter(owner=user)
        print("here first", players_lists)
        data = [{'id': plist.id, 'title': plist.title}
                for plist in players_lists]
        return JsonResponse({'players_lists': players_lists}, encoder=PlayerListEncoder)


@login_required
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
            return redirect('players_lists')
    else:
        form = PlayersListForm()
        context = {
            'form': form,

        }
        return render(request, 'players_lists/create_players_list.html',
                      context)


@login_required
def players_list_detail(request, id):
    list = get_object_or_404(PlayersList, id=id)
    context = {'list': list}
    return render(request, 'players_lists/players_list_detail.html', context)


def delete_list(request, id):
    item = get_object_or_404(PlayersList, id=id)
    item.delete()
    return redirect("players_lists")


@login_required
def delete_player(request, list_id, player_id,):
    player = get_object_or_404(Player, id=player_id)
    player.delete()
    return redirect("players_list_detail", id=list_id)


@login_required
def save_player(request, id, player_name):
    print("IM inside!")
    list = get_object_or_404(PlayersList, id=id)

    Player.objects.create(
        name=player_name, owner=request.user, player_list=list)

    return redirect("players_list_detail", id=id)


def search(request):
    query = None
    player_results = []
    emptyForm = SearchForm()
    message = None
    if request.user.is_authenticated:
        all_my_players = Player.objects.filter(owner=request.user)
        emptyForm = SearchForm()
        query = None
        player_results = []

        if request.method == "POST":
            form = SearchForm(request.POST)
            if form.is_valid():
                query = form.cleaned_data["q"]
                player_results = all_my_players.filter(
                    Q(name__icontains=query))
                print(player_results)
    else:
        message = "You need to log in in order to perform a search"
    context = {
        "query": query,
        "player_results": player_results,
        "search_form": emptyForm,
        "message": message,
    }
    return render(request, "players_lists/results.html", context)
