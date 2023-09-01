from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=255)
    players = models.PositiveSmallIntegerField()
    duration = models.PositiveSmallIntegerField()
    designer = models.CharField(max_length=255)
    description = models.TextField()
    

    def __str__(self) -> str:
        return self.title
