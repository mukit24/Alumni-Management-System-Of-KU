from unicodedata import name
from django.urls import path
from .views import HomePageView,profile_view, create_profile

app_name = 'home'
urlpatterns = [
    path('', HomePageView.as_view(), name='home_view'),
    path('profile/<int:id>/',profile_view, name='profile_view'),
    path('create_profile/<int:id>/',create_profile,name='create_profile'),
]
