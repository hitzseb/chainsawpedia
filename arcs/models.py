from django.db import models

from sagas.models import Saga

class Arc(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    saga = models.ForeignKey(Saga, on_delete=models.SET_NULL, null=True, related_name='arcs')

    def __str__(self):
        return f'(Number: {self.number}, Title: {self.title}, Saga: {self.saga.title})'