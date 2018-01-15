from rest_framework import serializers

from ..models import Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Comment
        fields = (
            'id',
            'board_id',
            'email',
            'name',
            'description',
            'created',
            'updated',
        )