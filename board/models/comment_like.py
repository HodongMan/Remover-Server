from django.db import models

from .comment import Comment

class CommentLike(models.Model):

    comment_id = models.ForeignKey(
        Comment,
        related_name='comment_like',
        on_delete=models.CASCADE,
    )
    user = models.CharField(max_length=200)

    class Meta:
        
        ordering = ('-comment_id',)
        unique_together = (('comment_id', 'user'),)