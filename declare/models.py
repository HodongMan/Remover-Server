from django.db import models
from board.models import Board


class Declare(models.Model):

    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()

    board_id = models.ForeignKey(
        Board,
        related_name='board_declare',
        on_delete=models.CASCADE,
        default=1
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ('-created',)