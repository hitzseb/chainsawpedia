from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from animes.models import Anime
from animes.serializers import AnimeSerializer

class AnimeList(APIView):
    def get(self, request):
        anime_list = Anime.objects.all().order_by('number')
        serializer = AnimeSerializer(anime_list, many=True)
        return Response(serializer.data)
