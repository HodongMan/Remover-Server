from django.db import models

class Category(models.Model):

    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, default="")
    background_color = models.CharField(max_length=200, default="")
    color = models.CharField(max_length=200, default="")

    created = models.DateTimeField(auto_now_add=True)


    class Meta:

        ordering = ("title",)