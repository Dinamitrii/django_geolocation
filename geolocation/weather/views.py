import requests
from django.shortcuts import render
import json


# Create your views here.

def get_current_weather(json_data, city):
    # ###
    # ip = requests.get('https://api.ipify.org?format=json')
    # ip_data = json.loads(ip.text)
    #
    # ###
    # res = requests.get('http://ip-api.com/json/', {'data': ip_data})
    # text_data = res.text
    # json_data = json.loads(text_data)
    # ###

    weather_url = (f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&lang=bg'
        f'&units=metric')

    data = requests.get(weather_url)
    text_weather = data.text
    weather = json.loads(text_weather)

    city = json_data['city']
    # Check for empty strings or string with only spaces
    if not bool(city.strip):
        city = json_data['city']

    return render(weather, 'weather.html', {'data': weather})
