from rest_framework import serializers
from .models import Manga

class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['number', 'title', 'volume']

class MangaDetailSerializer(serializers.ModelSerializer):
    arc_title = serializers.CharField(source='arc.title', read_only=True)
    class Meta:
        model = Manga
        fields = ['number', 'title', 'date', 'plot', 'source', 'volume', 'arc_title']