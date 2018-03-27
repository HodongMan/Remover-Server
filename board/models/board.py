from django.db import models

from .category import Category
from user.models import User

class Board(models.Model):

    category_id = models.ForeignKey(
        Category,
        related_name='category_board',
        on_delete=models.CASCADE,
    )
    user_id = models.ForeignKey(
        User,
        related_name='user_board',
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    image_url = models.CharField(max_length=200, default="")
    background_color = models.CharField(max_length=200, default="")
    color = models.CharField(max_length=200, default="")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        
        ordering = ('-created',)

