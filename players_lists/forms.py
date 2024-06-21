from django import forms
from django.forms import ModelForm
from .models import PlayersList, Player


class PlayersListForm(forms.ModelForm):
    # new_player_name = forms.CharField(
    #     label='New Player', max_length=100, required=False)

    class Meta:
        model = PlayersList
        fields = ['title']

    # def clean_new_player_name(self):
    #     name = self.cleaned_data.get('new_player_name')
    #     if name:
    #         # Check if the player with this name already exists
    #         if Player.objects.filter(name=name).exists():
    #             raise forms.ValidationError('This player already exists.')
    #     return name

    # def save(self, commit=True):
    #     players_list = super().save(commit=False)
    #     new_player_name = self.cleaned_data.get('new_player_name')
    #     if new_player_name:
    #         player = Player.objects.create(name=new_player_name)
    #         players_list.players_list.add(player)
    #     if commit:
    #         players_list.save()
    #     return players_list
