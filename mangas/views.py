from django.shortcuts import get_object_or_404, render
from mangas.models import Manga

def manga_detail(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    return render(request, 'manga_detail.html', {'manga': manga})
