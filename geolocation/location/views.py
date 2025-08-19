from django.shortcuts import render
import requests
import json


# Create your views here.
def index(request):
    ###
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)

    ###
    res = requests.get('http://ip-api.com/json/',{'data':ip_data})
    text_data = res.text
    json_data = json.loads(text_data)
    ###
    return render(request, 'index.html', {'data':json_data})
