from rest_framework import serializers
from .models import Memorial, GalleryImage, Footprint
from django.contrib.auth import get_user_model

User = get_user_model()

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'

class FootprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footprint
        fields = '__all__'

class MemorialSerializer(serializers.ModelSerializer):
    gallery_images = GalleryImageSerializer(many=True, read_only=True)
    footprints = FootprintSerializer(many=True, read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    new_gallery_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Memorial
        fields = [
            'id', 'user_id', 'pet_name', 'birth_date', 'death_date', 
            'memorial_name', 'memorial_tagline', 'main_image', 'message', 
            'gallery_images', 'footprints', 'new_gallery_images', 'created_at'
        ]

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        new_gallery_images = validated_data.pop('new_gallery_images', [])
        memorial = Memorial.objects.create(user=user, **validated_data)
        for image in new_gallery_images:
            GalleryImage.objects.create(image=image, memorials=memorial)
        return memorial

    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        new_gallery_images = validated_data.pop('new_gallery_images', [])
        if user_id:
            instance.user = User.objects.get(id=user_id)
        instance = super().update(instance, validated_data)
        for image in new_gallery_images:
            GalleryImage.objects.create(image=image, memorials=instance)
        return instance
