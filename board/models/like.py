from django.db import models

from .board import Board

class Like(models.Model):

    board_id = models.ForeignKey(
        Board,
        related_name='board',
        on_delete=models.CASCADE,
    )
    email = models.CharField(max_length=200)

    class Meta:
        
        ordering = ('-board_id',)