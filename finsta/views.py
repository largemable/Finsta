from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import FinstaEntry
from .serializers import FinstaEntrySerializer
from django.views import View
from django.http import HttpResponse


class FinstaImageUploadView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello World')
# Create your views here.


class FinstaEntryViewSet(viewsets.ModelViewSet):
    queryset = FinstaEntry.objects.all()
    # def get_queryset(self):
    #     user = self.request.user
    #     return FinstaEntry.objects.filter(user=user)
    serializer_class = FinstaEntrySerializer
