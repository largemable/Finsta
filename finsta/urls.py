# users/urls.py
from django.urls import path, include
from finsta import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken'))
]
