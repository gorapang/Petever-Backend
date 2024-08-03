from django.urls import path, include
from .views import MemorialViewSet,GalleryImageViewSet, FootprintViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'memorial', MemorialViewSet)
router.register(r'galleryimages', GalleryImageViewSet)
router.register(r'footprints', FootprintViewSet)

urlpatterns = [
    path('', include(router.urls)),
]