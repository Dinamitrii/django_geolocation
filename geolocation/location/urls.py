from django.urls import path
from weather import
from location import views


urlpatterns = [
    path('',views.index, name='index'),

    ]
