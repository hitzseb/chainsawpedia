from django.contrib import admin
from .models import Volume

@admin.register(Volume)
class Volume(admin.ModelAdmin):
    pass
