from django.shortcuts import get_object_or_404, render
from animes.models import Anime
from seasons.models import Season

def anime_list(request, pk):
    season = get_object_or_404(Season, pk=pk)
    anime_list = Anime.objects.filter(season=season).order_by('number')
    return render(request, 'anime_list.html', {'anime_list': anime_list})
