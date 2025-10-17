from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField()
    descriptions=models.CharField()

    def __str__(self):
        return self.name