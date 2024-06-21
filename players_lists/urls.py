from django.urls import path
from players_lists.views import players_lists, players_list_create, players_list_detail, delete_player, save_player

urlpatterns = [
    path("", players_lists, name="home"),
    path("<int:id>/", players_list_detail, name="players_list_detail"),
    path("delete_player/<int:list_id>/<int:player_id>",
         delete_player, name="delete_player"),
    path("create/", players_list_create, name="players_list_create"),
    path("<int:id>/save_player/<str:player_name>/",
         save_player, name="save_player")
]
