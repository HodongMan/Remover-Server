from rest_framework import serializers

from ..models import Comment, CommentLike
from user.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:

        model = Comment
        fields = (
            'id',
            'board_id',            
            'user',
            'user_id',
            'description',
            'like_count',
            'created',
            'updated',
        )

    def get_like_count(self, obj):

        return CommentLike.objects.filter(comment_id=obj.id).count()
