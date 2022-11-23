from functools import wraps
from django.http import HttpResponseRedirect
from django.urls import reverse

def check_profile(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        try:
            if request.user.alumni_profile and request.user.alumni_profile.is_verified:
                return function(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse('home:profile_view',args=(request.user.id,)))
        except:
            print('yoo')
            return HttpResponseRedirect(reverse('home:profile_view',args=(request.user.id,)))
  return wrap