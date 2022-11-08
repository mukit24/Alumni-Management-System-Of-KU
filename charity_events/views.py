from django.shortcuts import render
from django.views.generic import ListView
from .models import Event
# Create your views here.
class IndexView(ListView):
    model = Event
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['closed_events'] = Event.objects.filter(running=False)
        return context

    template_name = 'charity_events/index.html'