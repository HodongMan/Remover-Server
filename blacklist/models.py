from django.db import models


class BlackList(models.Model):

    user = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)