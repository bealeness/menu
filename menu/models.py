from django.db import models
from django.conf import settings


class Item(models.Model):

    options = (
        ('breakfast', "Breakfast"),
        ('lunch', "Lunch"),
        ('special', "Special"),
        ('snack', "Snack"),
        ('side', "Side"),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=20, choices=options)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items'
    )

    def __str__(self):
        return self.name

