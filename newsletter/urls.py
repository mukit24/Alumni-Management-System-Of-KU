from django.urls import path
from .views import index_view,news_details
app_name = 'newsletter'
urlpatterns = [
    path('<int:id>/',index_view, name='index'),
    path('news_details/<int:id>/',news_details, name='news_details'),
]
