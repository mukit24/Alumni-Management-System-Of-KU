from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Event
# Create your views here.
class IndexView(ListView):
    model = Event
    queryset = Event.objects.order_by('-running','created_on')
    template_name = 'charity_events/index.html'

class DetailView(DetailView):
    model = Event
    template_name = 'charity_events/details.html'

