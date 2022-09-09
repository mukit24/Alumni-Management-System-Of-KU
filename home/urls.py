from unicodedata import name
from django.urls import path
from .views import HomePageView, profile_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/<int:id>',profile_view,name='profile'),
]
