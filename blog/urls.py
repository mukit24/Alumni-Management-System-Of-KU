from django.urls import path
from .views import blog_index,create_post, post_detials, edit_post, delete_post
app_name = 'blog'
urlpatterns = [
    path('',blog_index,name='blog_index'),
    path('create_post/',create_post,name='create_post'),
    path('details/<int:id>/',post_detials,name='post_details'),
    path('edit/<int:id>',edit_post,name='edit_post'),
    path('delete/<int:id>',delete_post,name='delete_post'),
]
