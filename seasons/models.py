from django.db import models

class Season(models.Model):
    number = models.IntegerField(null=True, blank=True)
    trailer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'(Number: {self.number}, Trailer: {self.trailer})'
