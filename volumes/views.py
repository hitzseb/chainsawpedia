from django.shortcuts import render
from mangas.models import Manga
from .models import Volume

def volume_list(request):
    volume_list = Volume.objects.all().order_by('number')
    
    for volume in volume_list:
        manga_list = Manga.objects.filter(volume=volume).order_by('number')
        setattr(volume, 'manga_list', manga_list)

    context = {'volume_list': volume_list}
    return render(request, 'volume_list.html', context)
