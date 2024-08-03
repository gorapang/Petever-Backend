from django.shortcuts import render
from .serializers import MemorialSerializer
from rest_framework.viewsets import ModelViewSet
from . models import Memorial

class MemorialViewSet(ModelViewSet):
    queryset = Memorial.objects.all()
    serializer_class = MemorialSerializer


