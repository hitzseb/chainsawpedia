from django.contrib import admin
from .models import Anime

@admin.register(Anime)
class Anime(admin.ModelAdmin):
    pass