from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from volumes.serializers import VolumeSerializer
from mangas.models import Manga
from .models import Volume

class VolumeView(APIView):
    def get(self, request):
        volume_list = Volume.objects.all().order_by('number')
        serializer = VolumeSerializer(volume_list, many=True)
        return Response(serializer.data)

def volume_list(request):
    volume_list = Volume.objects.all().order_by('number')
    
    for volume in volume_list:
        manga_list = Manga.objects.filter(volume=volume).order_by('number')
        setattr(volume, 'manga_list', manga_list)

    context = {'volume_list': volume_list}
    return render(request, 'volume_list.html', context)
