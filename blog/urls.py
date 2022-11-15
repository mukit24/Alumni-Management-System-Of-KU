from django.urls import path
from .views import blog_index,create_post, post_detials, edit_post, delete_post, create_comment, edit_comment, delete_comment
app_name = 'blog'
urlpatterns = [
    path('',blog_index,name='blog_index'),
    path('create_post/',create_post,name='create_post'),
    path('details/<int:id>/',post_detials,name='post_details'),
    path('edit/<int:id>',edit_post,name='edit_post'),
    path('delete/<int:id>',delete_post,name='delete_post'),
    path('create_comment/<int:id>',create_comment, name='create_comment'),
    path('edit_comment/<int:id>',edit_comment,name='edit_comment'),
    path('delete_comment/<int:id>',delete_comment,name='delete_comment'),
]
