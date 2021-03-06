from django.db import models

class Board(models.Model):

    user = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    image_url = models.CharField(max_length=200, default="")
    background_color = models.CharField(max_length=200, default="")
    color = models.CharField(max_length=200, default="")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ('-pk',)