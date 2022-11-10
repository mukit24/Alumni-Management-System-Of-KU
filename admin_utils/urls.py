from django.urls import path
from .views import profile_verification,profile_operation_accept,profile_operation_reject
app_name = 'admin_utils'
urlpatterns = [
    path('profile-verification/',profile_verification,name='profile-verification'),
    path('profile-verification/<int:id>/accept/',profile_operation_accept,name='op_accept'),
    path('profile-verification/<int:id>/rejept/',profile_operation_reject,name='op_reject'),
]
