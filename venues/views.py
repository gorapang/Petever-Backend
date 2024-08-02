from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import FuneralSerializer
from .models import *

class FuneralViewSet(ModelViewSet):
    queryset = Funeral.objects.all()
    serializer_class = FuneralSerializer