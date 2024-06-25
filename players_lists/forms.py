from django import forms
from django.forms import ModelForm
from .models import PlayersList, Player


class PlayersListForm(forms.ModelForm):
    class Meta:
        model = PlayersList
        fields = ['title']
        labels = {
            'title': 'List Title',
        }


class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"placeholder": "Search for a player..."}),
        label="",
    )
