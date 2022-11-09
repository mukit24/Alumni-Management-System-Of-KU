from django.shortcuts import render
from django.views.generic import ListView
from home.models import Alumni_Profile
from .decorators import check_superuser
# Create your views here.
@check_superuser
def profile_verification(request):
    profiles = Alumni_Profile.objects.filter(is_verified=False)
    return render(request,'admin_utils/profile_verify.html',{'alumni_profile_list':profiles})
    