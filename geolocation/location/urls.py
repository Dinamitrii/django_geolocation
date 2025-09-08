from django.urls import path
from location import views


urlpatterns = [
    path('',views.index, name='index'),
    path('save-location/', views.save_location, name='update_location'),

    ]
