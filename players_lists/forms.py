from django import forms
from django.forms import ModelForm
from .models import PlayersList, Player


class PlayersListForm(forms.ModelForm):
    # new_player_name = forms.CharField(
    #     label='New Player', max_length=100, required=False)

    class Meta:
        model = PlayersList
        fields = ['title']


class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"placeholder": "Search for a player..."}),
        label="",
    )
