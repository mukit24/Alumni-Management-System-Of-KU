from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import Event,Contributer
from django.contrib.auth.decorators import login_required
from home.decorators import check_profile
# Create your views here.
class IndexView(ListView):
    model = Event
    queryset = Event.objects.order_by('-running','created_on')
    template_name = 'charity_events/index.html'

class DetailView(DetailView):
    model = Event
    template_name = 'charity_events/details.html'

@login_required
@check_profile
def add_money(request,id):
    print(request.POST)
    amount = int(request.POST['amount'])
    event = Event.objects.get(id=id)
    print(amount)
    if amount:
        contributer = Contributer(
            alumni=request.user.alumni_profile,
            event = event,
            amount=amount,
        )
        contributer.save()
        event.present_amount += amount
        event.save()
    return redirect('charity_events:detail_view', pk=id)

