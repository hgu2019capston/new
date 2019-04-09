from django.db import models


class Stone(models.Model):
    turn = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()

# Create your models here.
