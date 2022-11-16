from audioop import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from home.models import Alumni_Profile
from .forms import ProfileForm
from django.db.models import Q
from charity_events.models import Event

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

def discipline_view(request):
    discipline = request.user.alumni_profile.discipline
    total_alumni = Alumni_Profile.objects.filter(Q(discipline=discipline) & Q(is_verified=True)).count()

    batch = list(Alumni_Profile.objects.values_list('batch',flat=True).filter(Q(is_verified=True) & Q(discipline=discipline)))
    batch.sort()
    batch.insert(0,f'All (in {discipline})')

    events = Event.objects.filter(discipline=discipline)
    print(events)

    context = {
        'discipline':discipline,
        'total_alumni': total_alumni,
        'batches': batch,
        'events':events,
    }
    return render(request,'home/discipline_view.html',context)

def search_result_discipline(request):
    batch = request.POST['batch']
    discipline = request.user.alumni_profile.discipline
    if batch == f'All (in {discipline})':
        profiles = Alumni_Profile.objects.filter(Q(is_verified=True) & Q(discipline=discipline))
    else:
        profiles = Alumni_Profile.objects.filter(Q(is_verified=True) & Q(discipline=discipline) & Q(batch=batch))
    context = {
        'profiles':profiles,
    }
    
    return render(request,"search/search_results.html",context)


