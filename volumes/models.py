from django.db import models

class Volume(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    cover = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'(Number: {self.number}, Title: {self.title}, Date: {self.date}, Cover: {self.cover}'
