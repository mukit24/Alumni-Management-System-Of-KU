from django.urls import path
from .views import IndexView, event_details, add_money, payment_success
app_name = 'charity_events'

urlpatterns = [
    path('',IndexView.as_view(),name='index_view'),
    path('<int:id>/',event_details,name='detail_view'),
    path('<int:id>/add_money',add_money,name='add_money'),
    path('<int:id>/payment_success/<int:user_id>/',payment_success,name='success_payment'),
]
