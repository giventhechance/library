from django.urls import path

from people.views import *

app_name = 'people'
urlpatterns = [
    path('main_page/', main_page, name='main_page'),
    path('readers_list/', readers_list, name='readers_list'),
    path('add_reader/', add_reader, name='add_reader'),
]