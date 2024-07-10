from django.shortcuts import render
from rest_framework import generics
from dashboard.models import *
from dashboard.serializers import DataSerializer

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')


class DataListCreate(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


