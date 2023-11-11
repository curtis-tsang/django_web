from django.shortcuts import render
from django.http import HttpResponse

import requests
import json
from urllib.request import urlopen

# Create your views here.
def index(request):
    
    url = "http://api.weatherapi.com/v1/current.json?key=96800c7e19ec4ca3a4f93646232506&q=HK&aqi=no"
    response = urlopen(url)

    data = json.loads(response.read())

    location_key = ['name','lat','lon','localtime']
    location_data = []
    current_key = ['last_update','temp_c','wind_kph','wind_dir','humidity','feelslike_c','vis_km','uv']
    current_data = []
    dict_ = {}
    for key, item in data.items():
        if(key == 'location'):
            for x in ['name','lat','lon','localtime']:
                location_data.append(item[x])
        if(key == 'current'):
            for x in ['last_updated','temp_c','wind_kph','wind_dir','humidity','feelslike_c','vis_km','uv']:
                current_data.append(item[x])
                dict_.update({x:item[x]})
    
    print(dict_)

    
    
    return render(request, 'index.html', {'location_key': location_key, 'location_data': location_data, 'current_key': current_key, 'current_data': current_data, 'dict': dict_})



#0,3,4,7,2,3,8,10,15,17,19,21