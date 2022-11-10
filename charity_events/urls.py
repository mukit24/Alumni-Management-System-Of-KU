from django.urls import path
from .views import IndexView, DetailView, add_money
app_name = 'charity_events'

urlpatterns = [
    path('',IndexView.as_view(),name='index_view'),
    path('<int:pk>/',DetailView.as_view(),name='detail_view'),
    path('<int:id>/add_money',add_money,name='add_money'),
]
