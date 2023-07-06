from rest_framework import serializers
from .models import Arc

class ArcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arc
        fields = ['number', 'title', 'saga']