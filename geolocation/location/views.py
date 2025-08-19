from dotenv import load_dotenv
import os
from django.shortcuts import render
import requests
import json

from requests import request

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


    city = input("Enter city: ")

    weather_url = (
        f'https://api.openweathermap.org/data/2.5/weather?'
        f'appid={os.getenv("API_KEY")}&q={city}&lang=bg'
        f'&units=metric'
    )

    weather_data = requests.get(weather_url)

    weather_text = weather_data.text

    weather_json = json.loads(weather_text)

    return render(request, 'index.html', {'data': weather_json})


# def weather(request):
#
#     # city = input("Enter city: ")
#
#     weather_url = (
#         f'https://api.openweathermap.org/data/2.5/weather?'
#         f'appid={os.getenv("API_KEY")}&q={index(request).getvalue()}&lang=bg'
#         f'&units=metric'
#     )
#
#     weather_data = requests.get(weather_url)
#
#     weather_text = weather_data.text
#
#     weather_json = json.loads(weather_text)
#
#     return render(request, 'weather.html', {'data': weather_json})
