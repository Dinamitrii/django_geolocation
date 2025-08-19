from django.urls import path
from location import views
from weather import admin

urlpatterns = [
    path('',views.weather, name='weather.html'),
    ]
