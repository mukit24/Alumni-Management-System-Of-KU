from django.shortcuts import render,redirect
from django.views.generic import ListView
from home.models import Alumni_Profile
from .decorators import check_superuser
from AMSKU.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.
@check_superuser
def profile_verification(request):
    profiles = Alumni_Profile.objects.filter(is_verified=False)
    return render(request,'admin_utils/profile_verify.html',{'alumni_profile_list':profiles})

def profile_operation_accept(request,id):
    profile = Alumni_Profile.objects.get(pk=id)
    profile.is_verified=True
    profile.save()

    subject = 'Verification of Alumni'
    message = 'Congrats '+str(profile.full_name)+'! Your Verification is done...Enjoy Our Services...'
    recepient = str(profile.user.email)
    send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return redirect('admin_utils:profile-verification')

def profile_operation_reject(request,id):
    profile = Alumni_Profile.objects.get(pk=id)
    profile.delete()
    subject = 'Verification of Alumni'
    message = request.POST['message']
    recepient = str(profile.user.email)
    send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return redirect('admin_utils:profile-verification')
    