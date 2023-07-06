from rest_framework import serializers
from .models import Saga

class SagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saga
        fields = ['number', 'title']