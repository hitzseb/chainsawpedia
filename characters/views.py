from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from characters.models import Character
from characters.serializers import CharacterSerializer

class CharacterList(APIView):
    def get(self, request):
        character_list = Character.objects.all().order_by('-is_main', 'name')
        serializer = CharacterSerializer(character_list, many=True)
        return Response(serializer.data)

def character_list(request):
    character_list = Character.objects.all().order_by('-is_main', 'name')
    context = {'character_list': character_list}
    return render(request, 'character_list.html', context)

def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'character_detail.html', {'character': character})