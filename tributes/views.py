from django.shortcuts import render
from .serializers import MemorialSerializer, GalleryImageSerializer, FootprintSerializer
from rest_framework.viewsets import ModelViewSet
from . models import Memorial, GalleryImage, Footprint

class MemorialViewSet(ModelViewSet):
    queryset = Memorial.objects.all()
    serializer_class = MemorialSerializer

class GalleryImageViewSet(ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer

class FootprintViewSet(ModelViewSet):
    queryset = Footprint.objects.all()
    serializer_class = FootprintSerializer