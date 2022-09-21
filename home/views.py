from audioop import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView
from home.models import Alumni_Profile
from .forms import ProfileForm

# Create your views here.
class HomePageView(TemplateView):
    template_name='home/home.html'

def profile_view(request, id):
    profile_data = []
    try:
        profile_data = Alumni_Profile.objects.get(user=id)
    except:
        if request.user.id == id:
            return redirect('home:create_profile', id)
        else:
            pass
   
    context = {
        'profile': profile_data,
    }
    return render(request, "home/profile_view.html",context)

def create_profile(request,id):
    form = ProfileForm()
    if request.method == 'POST':
        print('yoo')
        form = ProfileForm(request.POST, request.FILES)
        print('yoo')
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            new_alumni = form.save(commit=False)
            new_alumni.user = request.user
            new_alumni.save()
            form.save_m2m()
            print('yoo')
            return redirect('home:profile_view', id)

    context = {
        'form': form,
    }
    return render(request,"home/create_profile.html",context)

def update_profile(request, id):
    profile = Alumni_Profile.objects.get(user=id)
    form = ProfileForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home:profile_view', id)

    context = {
        "form": form
    }
    return render(request, "home/update_profile.html", context)


