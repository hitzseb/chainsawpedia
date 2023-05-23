from django.contrib import admin
from .models import Manga

@admin.register(Manga)
class Manga(admin.ModelAdmin):
    pass
