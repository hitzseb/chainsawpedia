from django.db import models
from arcs.models import Arc

class Volume(models.Model):
    number = models.IntegerField(null=True, blank=True)
    cover = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'(Number: {self.number}, Cover: {self.cover}'
