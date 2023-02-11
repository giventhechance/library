from django.urls import path

from people.views import *

app_name = 'people'
urlpatterns = [
    path('readers_list/', readers_list, name='readers_list'),
]