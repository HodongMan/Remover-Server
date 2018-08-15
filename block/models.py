from django.db import models

class BlockUser(models.Model):

    from_user = models.CharField(max_length=200)
    to_user = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        
        ordering = ('-created', 'from_user')