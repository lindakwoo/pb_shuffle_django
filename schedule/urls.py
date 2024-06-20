from django.urls import path
from schedule.views import list_games

urlpatterns = [
    path("", list_games, name="list_games"),
]
