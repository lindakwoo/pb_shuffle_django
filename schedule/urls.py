from django.urls import path
from schedule.views import list_games

urlpatterns = [
    path("<int:id>/", list_games, name="list_games"),

]
