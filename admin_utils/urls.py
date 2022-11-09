from django.urls import path
from .views import profile_verification
app_name = 'admin_utils'
urlpatterns = [
    path('profile-verification/',profile_verification,name='profile-verification')
]
