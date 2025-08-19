from django.shortcuts import render
import requests
import json


# Create your views here.
def index(request):
    res = requests.get('http://ip-api.com/json/24.48.0.1')
    text_data = res.text
    json_data = json.loads(text_data)

    return render(request, 'index.html', {'data':json_data})
