from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import FinstaEntry
from .serializers import FinstaEntrySerializer
from django.views import View
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import logging as LOG

# Create your views here.


class FinstaEntryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        print(f'USERNAME IS {self.request.user.username}')
        user = self.request.user
        return FinstaEntry.objects.filter(user=user)
    serializer_class = FinstaEntrySerializer
