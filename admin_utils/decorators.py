from functools import wraps
from django.http import HttpResponseRedirect

def check_superuser(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
  return wrap
