from django.shortcuts import render
from animes.models import Anime
from .models import Season

def season_list(request):
    season_list = Season.objects.all().order_by('number')
    
    for season in season_list:
        anime_list = Anime.objects.filter(season=season).order_by('number')
        setattr(season, 'anime_list', anime_list)

    context = {'season_list': season_list}
    return render(request, 'season_list.html', context)