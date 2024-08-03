from django.shortcuts import render
from .serializers import MemorialSerializer, GalleryImageSerializer, FootprintSerializer, MemorialListSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Memorial, GalleryImage, Footprint
from rest_framework.parsers import MultiPartParser, FormParser


class MemorialViewSet(ModelViewSet):
    queryset = Memorial.objects.all()
    parser_classes = (MultiPartParser, FormParser)

    def get_serializer_class(self):
        if self.action == 'list':
            return MemorialListSerializer
        return MemorialSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        return super(MemorialViewSet, self).get_permissions()


class GalleryImageViewSet(ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer


class FootprintViewSet(ModelViewSet):
    queryset = Footprint.objects.all()
    serializer_class = FootprintSerializer
