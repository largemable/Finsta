from django.shortcuts import render
from rest_framework import viewsets
from .models import FinstaEntry
from .serializers import FinstaEntrySerializer
# Create your views here.


class FinstaEntryViewSet(viewsets.ModelViewSet):
    queryset = FinstaEntry.objects.all()
    serializer_class = FinstaEntrySerializer
