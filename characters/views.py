from django.shortcuts import get_object_or_404, render
from characters.models import Character

def character_list(request):
    character_list = Character.objects.all().order_by('-is_main', 'name')
    context = {'character_list': character_list}
    return render(request, 'character_list.html', context)

def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'character_detail.html', {'character': character})