# from django.contrib import admin
# from .models import Review

#admin.site.register(Review)
from django.contrib import admin
from .models import Memorial, GalleryImage, Footprint

@admin.register(Memorial)
class MemorialAdmin(admin.ModelAdmin):
    list_display = ('memorial_name', 'birth_date', 'death_date', 'created_at')
    search_fields = ('memorial_name', 'message')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at')
    search_fields = ('id',)

@admin.register(Footprint)
class FootprintAdmin(admin.ModelAdmin):
    list_display = ('username', 'memorial', 'created_at')
    search_fields = ('username', 'content')
