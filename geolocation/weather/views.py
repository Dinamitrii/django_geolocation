from dotenv import load_dotenv
import os
from django.shortcuts import render
import requests
import json

from requests import request

load_dotenv('.env')
BASE_URL = os.getenv("BASE_URL")


def get_current_weather(city):

    weather_url = (
        f'https://api.openweathermap.org/data/2.5/weather?'
        f'appid={os.getenv("API_KEY")}&q={city}&lang=bg'
        f'&units=metric'
    )

    weather_data = requests.get(weather_url)

    weather_text = weather_data.text

    weather_json = json.loads(weather_text)

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Sofia"


    return render(request, 'weather.html', {'data': weather_json, 'city': city})
