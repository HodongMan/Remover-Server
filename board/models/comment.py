from django.db import models

from .board import Board
from user.models import User

class Comment(models.Model):

    board_id = models.ForeignKey(
        Board,
        related_name='board_comment',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        related_name='user_comment',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:

        ordering = ('board_id', '-created',)