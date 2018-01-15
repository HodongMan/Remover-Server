from django.db import models

class Board(models.Model):

    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    vies = models.PositiveIntegerField()
    image_url = models.CharField(max_length=200, default="")
    background_color = models.CharField(max_length=200, default="")
    color = models.CharField(max_length=200, default="")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ('-pk')