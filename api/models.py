from django.db import models

# Create your models here.
class StreamPlatform(models.Model):
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=50)
    website=models.URLField(max_length=300)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title=models.CharField(max_length=30)
    storyline=models.CharField(max_length=300)
    active=models.BooleanField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
