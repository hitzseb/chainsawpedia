from rest_framework import serializers
from .models import Character

class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'image']

class CharacterDetailSerializer(serializers.ModelSerializer):
    manga_debut = serializers.IntegerField(source='manga_debut.number', read_only=True)
    anime_debut = serializers.IntegerField(source='anime_debut.number', read_only=True)
    class Meta:
        model = Character
        fields = ['name', 'image', 'description', 'appearance', 'human_form', 'fiend_form', 'hybrid_form', 'devil_form', 'personality', 'powers_and_abilities', 'source', 'alias', 'species', 'age', 'height', 'birthday', 'birthplace', 'status', 'contracted_devils', 'contracted_humans', 'is_main', 'manga_debut', 'anime_debut']