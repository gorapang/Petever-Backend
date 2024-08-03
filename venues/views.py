from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import FuneralSerializer
from .models import Funeral

class FuneralViewSet(ModelViewSet):
    queryset = Funeral.objects.all()
    serializer_class = FuneralSerializer

    # list 함수 오버라이딩
    def list(self, request, *args, **kwargs):
        region = request.query_params.get('region')
        if region:
            queryset = Funeral.objects.filter(region=region)
            if not queryset.exists():
                return Response(
                    {"error": "No funerals found for the specified region."},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
