from django.db import models

from .board import Board

class Like(models.Model):

    board_id = models.ForeignKey()
    email = models.CharField(max_lebgth=200)

    class Meta:
        
        ordering = ('-board_id')