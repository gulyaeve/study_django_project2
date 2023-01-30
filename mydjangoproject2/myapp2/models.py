from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=20, blank=False)
    number = models.IntegerField(default=50)

    def __str__(self):
        return self.name
