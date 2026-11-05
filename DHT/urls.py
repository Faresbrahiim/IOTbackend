from django.urls import path

from DHT import api
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
   
    path("api/get", api.Dlist, name='json'),
    path("api/post", api.Dhtviews.as_view(), name='json'),
]