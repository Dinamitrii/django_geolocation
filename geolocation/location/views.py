from dotenv import load_dotenv
import os
from django.shortcuts import render , get_object_or_404
import requests
import json
import folium


load_dotenv(".env")
BASE_URL = os.getenv("BASE_URL")


# Create your views here.
def index(request):
    ###
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)

    ###
    res = requests.get('http://ip-api.com/json/', {'data': ip_data})
    text_data = res.text
    json_data = json.loads(text_data)
    ###


    return render(request, 'base.html', {'data': json_data})


def loc_on_map(request):

    mp = folium.Map(location=[12.0, -9.0], zoom_start=9, tiles='street_map')
    folium.Marker(location=[12, -9], popup=folium.Popup(text_content="Hint...")).add_to(mp)
    folium.LayerControl().add_to(mp)

    return render(request, "index.html", {'map': mp})


def base(request):
    pass