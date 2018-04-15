from django.db import models

from .board import Board

class Like(models.Model):

    board_id = models.ForeignKey(
        Board,
        related_name='board_like',
        on_delete=models.CASCADE,
    )
    user = models.CharField(max_length=200)

    class Meta:
        
        ordering = ('-board_id',)
        unique_together = (('board_id', 'user'),)