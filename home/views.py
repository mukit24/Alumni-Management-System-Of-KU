from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ProfileForm
# Create your views here.
class HomePageView(TemplateView):
    template_name='home/home.html'

def profile_view(request,id):
    form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request,"home/profile_view.html",context)


