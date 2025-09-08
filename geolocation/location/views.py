from django.http import JsonResponse
from dotenv import load_dotenv
import os
from django.shortcuts import render , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from core.models import Location
import requests
import json
import folium


load_dotenv(".env")
BASE_URL = os.getenv("BASE_URL")


# Create your views here.
def index(request):
    context = {}
    ###
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)

    ###
    resp = requests.get('http://ip-api.com/json/', {'data': ip_data})
    text_data = resp.text
    json_data = json.loads(text_data)
    ###


    return render(request, 'index.html', context)


@login_required
def save_location(request):
    try:
        data = json.loads(request.body)
        # Extracting location data
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # Validating the data
        if not all([latitude, longitude]):
            return JsonResponse({
                'status': 'error',
                'message': 'Incomplete Location Data'
            }, status=400)

        # Saving User Data
        Location.objects.update_or_create(
            user=request.user,
            defaults={
                'latitude': latitude,
                'longitude': longitude,
            }
        )
        return JsonResponse({
            'status': 'success',
            'message': 'Location Saved'
        }, status=200)
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)



    mp = folium.Map(location=([19,-21]), zoom_start=9, tiles='Tile Terrain')
    folium.Marker(location=[12, -9], popup=folium.Popup(text_content="Hint...")).add_to(mp)
    folium.LayerControl().add_to(mp)

    return render(request, "index.html", {'map': mp})


