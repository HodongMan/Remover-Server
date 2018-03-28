from rest_framework import serializers

from ..models import Comment, CommentLike
from user.models import User
from user.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()
    user_id = UserSerializer(read_only=True)

    class Meta:

        model = Comment
        fields = (
            'id',
            'board_id',
            'user_id',
            'description',
            'like_count',
            'created',
            'updated',
        )

    def create(self, validated_data):
        
        user = self.context['request'].query_params['user']
        validated_data['user_id'] = User.objects.get(user=user)
        return Comment.objects.create(**validated_data)

    def get_like_count(self, obj):

        return CommentLike.objects.filter(comment_id=obj.id).count()
