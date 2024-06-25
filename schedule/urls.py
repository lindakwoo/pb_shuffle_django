from django.urls import path
from schedule.views import list_games, regenerate_schedule

urlpatterns = [
    path("<int:id>/", list_games, name="list_games"),
    path("<int:id>/regenerate/<int:num_courts>/",
         regenerate_schedule, name="regenerate_schedule"),
]
