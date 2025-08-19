from django.shortcuts import render
import requests
import json


# Create your views here.
def index(request):
    ###
    ip = request.META.get('REMOTE_ADDR')
    ip_data = requests.get('https://api.ipify.org')
    ip_data_dict = json.loads(ip_data.text)
    ###
    res = requests.get('http://ip-api.com/json/24.48.0.1')
    text_data = res.text
    json_data = json.loads(text_data)
    ###
    return render(request, 'index.html', {'data':json_data})
