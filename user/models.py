from django.db import models


class User(models.Model):

    user = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    profile_image = models.CharField(max_length=200)

    