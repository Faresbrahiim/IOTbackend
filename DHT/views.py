from django.shortcuts import render
from .models import Dht11

def dashboard(request):
    readings = list(Dht11.objects.exclude(temp__isnull=True).order_by('-dt')[:20])
    latest = readings[0] if readings else None
    return render(request, 'DHT/index.html', {'latest': latest, 'readings': readings})