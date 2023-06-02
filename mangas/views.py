from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from mangas.models import Manga
from mangas.serializers import MangaListSerializer, MangaDetailSerializer

class MangaView(APIView):
    def get(self, request, number=None):
        if number is None:
            manga_list = Manga.objects.all().order_by('number')
            serializer = MangaListSerializer(manga_list, many=True)
        else:
            manga = get_object_or_404(Manga, number=number)
            serializer = MangaDetailSerializer(manga)
        return Response(serializer.data)

def manga_detail(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    return render(request, 'manga_detail.html', {'manga': manga})
