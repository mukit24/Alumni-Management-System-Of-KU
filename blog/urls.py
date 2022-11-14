from django.urls import path
from .views import blog_index,create_post
app_name = 'blog'
urlpatterns = [
    path('',blog_index,name='blog_index'),
    path('<int:id>/create_post/',create_post,name='create_post'),
]
