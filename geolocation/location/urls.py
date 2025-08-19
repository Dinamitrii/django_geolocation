from django.urls import path
from weather import get_current_weather
from location import views


urlpatterns = [
    path('',views.index, name='index'),

    path('', views.get_current_weather(), name='weather'),
]