from django.db import models
from pickleball_shuffle import settings


class PlayersList(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="player_lists",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Player(models.Model):
    name = models.CharField(max_length=100)
    player_list = models.ForeignKey(
        'PlayersList', related_name='players', on_delete=models.CASCADE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="players",
        on_delete=models.CASCADE,
    )

    @property
    def player_list_title(self):
        return self.player_list.title

    class Meta:
        ordering = ['player_list__title', 'name']

    def __str__(self):
        return self.name
