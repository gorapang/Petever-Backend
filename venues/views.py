from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import FuneralSerializer
from .models import Funeral

class FuneralViewSet(ModelViewSet):
    queryset = Funeral.objects.all()
    serializer_class = FuneralSerializer

    # 권역별 필터링 함수
    def get_region_queryset(self, region):
        region_map = {
            '수도권': ['서울특별시', '고양시', '경기도'],
            '강릉권': ['강릉시', '강원도'],
            '충청권': ['충청북도', '충청남도', '세종특별자치시', '대전광역시'],
            '영남권': ['부산광역시', '대구광역시', '울산광역시', '경상북도', '경상남도'],
            '호남권': ['광주광역시', '전라북도', '전라남도']
        }
        if region in region_map:
            return self.queryset.filter(region__in=region_map[region])
        return None

    # list 함수 오버라이딩
    def list(self, request, *args, **kwargs):
        region = request.query_params.get('region')
        if region:
            queryset = self.get_region_queryset(region)
            if queryset is None:
                return Response(
                    {"error": "Invalid region specified."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            queryset = self.queryset

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
