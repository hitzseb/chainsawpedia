from django.db import models
from arcs.models import Arc
from volumes.models import Volume

class Manga(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    plot = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=50, null=True, blank=True)
    volume = models.ForeignKey(Volume, on_delete=models.SET_NULL, null=True, related_name='mangas')
    arc = models.ForeignKey(Arc, on_delete=models.SET_NULL, null=True, related_name='mangas')

    def __str__(self):
        return f'(Number: {self.number}, Title: {self.title}, Date: {self.date}, Plot: {self.plot}, Source: {self.source}, Volume: {self.volume.number}, Arc: {self.arc.title})'