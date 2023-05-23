from django.db import models
from arcs.models import Arc
from seasons.models import Season

class Anime(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    plot = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=50, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, related_name='animes')

    def __str__(self):
        return f'(Number: {self.number}, Title: {self.title}, Date: {self.date}, Plot: {self.plot}, Source: {self.source}, Season: {self.season.number}'