from django.db import models

class Saga(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'(Number: {self.number}, Title: {self.title}'
