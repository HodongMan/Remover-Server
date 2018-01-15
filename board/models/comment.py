from django.db import models

from .board import Board

class Comment(models.Model):

    board_id = models.ForeignKey(
        Board,
        related_name='board',
        on_delete=models.CASCADE,
    )
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:

        ordering = ('-board_id', '-created',)