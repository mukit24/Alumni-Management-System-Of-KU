from django.urls import path
from .views import IndexView
app_name = 'charity_events'

urlpatterns = [
    path('',IndexView.as_view(),name='index_view'),
]
