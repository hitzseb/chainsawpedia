from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from characters.models import Character
from characters.serializers import CharacterListSerializer, CharacterDetailSerializer

class CharacterView(APIView):
    def get(self, request, name=None):
        if name is None:
            character_list = Character.objects.all().order_by('-is_main', 'name')
            serializer = CharacterListSerializer(character_list, many=True)
        else:
            character = get_object_or_404(Character, Q(name__iexact=name))
            serializer = CharacterDetailSerializer(character)
        return Response(serializer.data)

def character_list(request):
    character_list = Character.objects.all().order_by('-is_main', 'name')
    context = {'character_list': character_list}
    return render(request, 'character_list.html', context)

def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'character_detail.html', {'character': character})