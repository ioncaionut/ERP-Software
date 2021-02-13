from django.db import models

# Create your models here.
class Ais(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title
