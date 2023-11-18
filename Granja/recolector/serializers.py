from rest_framework import serializers
from .models import Recolector

class RecolectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recolector
        fields = '__all__'
