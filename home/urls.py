from django.urls import path
from .views import HomePageView,profile_view, create_profile, update_profile,discipline_view, search_result_discipline

app_name = 'home'
urlpatterns = [
    path('', HomePageView.as_view(), name='home_view'),
    path('profile/<int:id>/',profile_view, name='profile_view'),
    path('create_profile/<int:id>/',create_profile,name='create_profile'),
    path('update_profile/<int:id>/',update_profile,name='update_profile'),
    path('discipline/',discipline_view,name='discipline_view'),
    path('discipline/search_results',search_result_discipline, name='search_result_discipline'),
]
