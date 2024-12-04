# droneapp/views.py
from django.http import JsonResponse
from django.shortcuts import render,redirect
import folium

def home(request):
    return redirect('dashboard')

def dashboard(request):
    return render(request, 'dashboard.html')

def map_view(request):
    my_map = folium.Map(location=[34.7406, 10.7603], zoom_start=12)
    map_html = my_map._repr_html_()  
    return render(request, 'map.html', {'map': map_html})



   






