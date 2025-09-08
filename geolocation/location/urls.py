from django.urls import path
from location import views


urlpatterns = [
    path('',views.index, name='index'),
    path('', views.base, name='base'),

    ]
