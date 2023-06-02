from rest_framework import serializers
from .models import Anime

class AnimeSerializer(serializers.ModelSerializer):
    season_number = serializers.IntegerField(source='season.number', read_only=True)
    class Meta:
        model = Anime
        fields = ['number', 'title', 'date', 'plot', 'source', 'season_number']