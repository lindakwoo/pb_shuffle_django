from django import template
from players_lists.forms import SearchForm

register = template.Library()


@register.inclusion_tag("search_form.html")
def show_search_form():
    return {"search_form": SearchForm()}
