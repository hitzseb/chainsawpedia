from django.contrib import admin
from .models import Saga

@admin.register(Saga)
class Saga(admin.ModelAdmin):
    pass
