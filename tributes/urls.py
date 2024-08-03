from django.urls import path, include
from .views import MemorialViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'memorial', MemorialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]