from django.contrib import admin
from .models import Memorial, GalleryImage, Footprint

@admin.register(Memorial)
class MemorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pet_name', 'birth_date', 'death_date', 'memorial_name', 'memorial_tagline', 'main_image', 'message', 'created_at')
    search_fields = ('memorial_name', 'message')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at')
    search_fields = ('id',)

@admin.register(Footprint)
class FootprintAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'username', 'memorial', 'created_at')
    search_fields = ('username', 'content')
