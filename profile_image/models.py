from django.db import models

class ProfileImage(models.Model):

    image_url = models.CharField(max_length=200)

    class Meta:

        ordering = ('image_url',)