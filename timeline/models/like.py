from django.db import models

class Like(models.Model):

    board_id = models.ForeignKey()
    email = models.CharField(max_length=200)

    class Meta:

        ordering = ('-board_id')