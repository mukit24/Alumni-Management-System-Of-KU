from django.urls import path
from .views import search_view, search_result, advance_search_results
app_name = 'search'

urlpatterns = [
    path('',search_view,name='search_view'),
    path('discipline_batch/',search_result, name='search_results'),
    path('keyword_search/',advance_search_results,name='advance_search'),
]
