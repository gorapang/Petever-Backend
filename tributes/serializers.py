from rest_framework import serializers
from .models import Memorial

class MemorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memorial
        fields = '__all__'