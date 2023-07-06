from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from animes.models import Anime
from .models import Season
from .serializers import SeasonSerializer

class SeasonView(APIView):
    def get(self, request):
        season_list = Season.objects.all().order_by('number')
        serializer = SeasonSerializer(season_list, many=True)
        return Response(serializer.data)
    

def season_list(request):
    season_list = Season.objects.all().order_by('number')
    
    for season in season_list:
        anime_list = Anime.objects.filter(season=season).order_by('number')
        setattr(season, 'anime_list', anime_list)

    context = {'season_list': season_list}
    return render(request, 'season_list.html', context)