from django.contrib import admin
from .models import Character

@admin.register(Character)
class Character(admin.ModelAdmin):
    pass
