from django.db import models

# Create your models here.
# Food
# - name
# - origin
# - date_of_expiry
# - recipe () -> ingredients


class Food(models.Model):
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    date_of_expiry = models.DateField()
    recipe = models.TextField()

    def __str__(self):
        return self.name
