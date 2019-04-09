from rest_framework import serializers
from .models import Stone

class OmokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stone
        fields = ('id', 'turn', 'x', 'y')

