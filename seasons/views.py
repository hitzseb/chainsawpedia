from django.shortcuts import render
from animes.admin import Anime
from .models import Season

def season_list(request):
    season_list = Season.objects.all().order_by('number')
    context = {'season_list': season_list}
    return render(request, 'season_list.html', context)
