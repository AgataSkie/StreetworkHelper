from django.views.generic import CreateView, ListView

from .models import Place


class PlaceListView(ListView):
    model = Place


class PlaceCreateView(CreateView):
    model = Place
    fields = (
        'city',
        'location',
    )
