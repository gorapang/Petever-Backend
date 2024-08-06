from django.shortcuts import render, get_object_or_404
from .serializers import MemorialSerializer, GalleryImageSerializer, FootprintSerializer, MemorialListSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Memorial, GalleryImage, Footprint
from rest_framework.parsers import MultiPartParser, FormParser

from django.contrib.auth import get_user_model
User = get_user_model()

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

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def user_memorials(self, request, user_id=None):
        """
        특정 유저가 생성한 memorial 조회`
        """
        user = get_object_or_404(User, id=user_id)
        memorials = self.queryset.filter(user=user)
        page = self.paginate_queryset(memorials)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(memorials, many=True)
        return Response(serializer.data)


class GalleryImageViewSet(ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer


class FootprintViewSet(ModelViewSet):
    queryset = Footprint.objects.all()
    serializer_class = FootprintSerializer
