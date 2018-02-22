from django.db import models

class BoardImage(models.Model):

    image_url = models.CharField(max_length=200)
    font_color = models.CharField(max_length=200)

    class Meta:

        ordering = ('id', )