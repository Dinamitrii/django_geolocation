from django.urls import path
from location import views
from weather import get_current_weather


urlpatterns = [
    path('',views.index, name='index'),
    path('', views.get_current_weather(get_current_weather()), name='weather'),
]