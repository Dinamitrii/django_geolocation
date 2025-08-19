from dotenv import load_dotenv
import segno
import os
from django.shortcuts import render
import requests
import json

from tornado.escape import json_decode

from location.qr_code_generator import link_to_qr_code

load_dotenv()


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

    return render(request, 'index.html', {'data': json_data})


def get_current_weather(request):
    ###
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)

    ###
    res = requests.get('http://ip-api.com/json/', {'data': ip_data})
    text_data = res.text
    json_data = json.loads(text_data)
    ###

    request_url = (f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={json_data['city']}&lang=bg'
                   f'&units=metric')
    data = requests.get(request_url).json()
    weather_data = json.loads(data.text)

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = json_data['city']

    # weather_data = get_current_weather(city)

    return render(weather_data, 'weather.html', {'data': weather_data}, )


# def link_to_qr_code(link):
#     # link make to qr here
#     qr_code = segno.make(link)
#     qr_code.save('static/images/qr_code.png', scale=4)
