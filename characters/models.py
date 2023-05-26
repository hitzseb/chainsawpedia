from django.db import models
from animes.models import Anime
from mangas.models import Manga

class Character(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.CharField(max_length=100 , null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    appearance = models.TextField(null=True, blank=True)
    human_form = models.TextField(null=True, blank=True)
    fiend_form = models.TextField(null=True, blank=True)
    hybrid_form = models.TextField(null=True, blank=True)
    devil_form = models.TextField(null=True, blank=True)
    personality = models.TextField(null=True, blank=True)
    powers_and_abilities = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    alias = models.TextField(null=True, blank=True)
    species = models.TextField(null=True, blank=True)
    age = models.TextField(null=True, blank=True)
    height = models.CharField(max_length=50 , null=True, blank=True)
    birthday = models.CharField(max_length=50, null=True, blank=True)
    birthplace = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    contracted_devils = models.TextField(null=True, blank=True)
    contracted_humans = models.TextField(null=True, blank=True)
    is_main = models.BooleanField(null=True, blank=True)
    manga_debut = models.ForeignKey(Manga, on_delete=models.SET_NULL, null=True, blank=True, related_name='characters')
    anime_debut = models.ForeignKey(Anime, on_delete=models.SET_NULL, null=True, blank=True, related_name='characters')

    def __str__(self):
        return f'(Name: {self.name}, Image: {self.image}, Description: {self.description}, Appearance: {self.appearance}, Human form: {self.human_form}, Fiend form: {self.fiend_form}, Hybrid form: {self.hybrid_form}, Devil form: {self.devil_form}, Personality: {self.personality}, Powers & abilities: {self.powers_and_abilities}, Source: {self.source}, Alias: {self.alias}, Species: {self.species}, Age: {self.age}, Height: {self.height}, Birthday: {self.birthday}, Birthplace: {self.birthplace}, Status: {self.status}, Contracted devils: {self.contracted_devils}, Contracted humans: {self.contracted_humans}, Manga debut: {self.manga_debut}, Anime debut: {self.anime_debut})'
