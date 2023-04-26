from django.urls import path
from . import views
app_name='search_app'

from . import views

urlpatterns = [
   path('',views.SearchResult,name='SearchResult')

]