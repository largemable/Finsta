# users/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FinstaEntryViewSet

router = DefaultRouter()
router.register(r'entries', FinstaEntryViewSet, basename='entries')
urlpatterns = [
    path('', include(router.urls)),
]
