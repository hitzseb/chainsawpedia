from django.contrib import admin
from .models import Arc

@admin.register(Arc)
class Arc(admin.ModelAdmin):
    pass
