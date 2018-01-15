from django.db import models

class Comment(models.Model):

    board_id = models.ForeignKey()
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ('-board_id')