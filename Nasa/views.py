from django.shortcuts import render
from django.http import HttpResponse
import requests as req

def Index(request):
    return render(request,'Home/index.html')

def Meteoro(request):
    print(request.GET['inicio'])
    KEY = 'SjFyKSTrGXT5sBWOCa2wmqt2xV9q4mbN6uDuE46x'
    r = req.get('https://api.nasa.gov/neo/rest/v1/feed', {'start_date':request.GET['inicio'], 'end_date':request.GET['fin'], 'api_key':KEY})
    print(r.url)
    meteoros = r.json()
    return render(request,'Home/meteoro.html',{'meteoros':meteoros['near_earth_objects']})