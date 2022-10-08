from django.db import models

class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False
    )
    description = models.CharField(
        max_length=120,
        unique=True,
        blank=True
    )
    quantity = models.IntegerField(

    )
