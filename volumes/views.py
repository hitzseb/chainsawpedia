from django.shortcuts import get_object_or_404, render
from mangas.models import Manga
from .models import Volume

def volume_list(request):
    volume_list = Volume.objects.all().order_by('number')
    context = {'volume_list': volume_list}
    return render(request, 'volume_list.html', context)

def volume_detail(request, pk):
    volume = get_object_or_404(Volume, pk=pk)
    mangas = Manga.objects.filter(volume=volume).order_by('number')
    return render(request, 'volume_detail.html', {'volume': volume, 'mangas': mangas})
