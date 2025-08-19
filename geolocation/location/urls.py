from django.urls import path

import weather
from location import views
from weather import get_current_weather


urlpatterns = [
    path('',views.index, name='index'),

    path('', weather.get_current_weather(), name='weather'),
]