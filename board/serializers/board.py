from rest_framework import serializers

from ..models import Board, Comment, Like


class BoardSerializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    comment_list = serializers.SerializerMethodField()

    class Meta:

        model = Board
        fields = (
            'id',
            'category_id',
            'user',
            'name',
            'description',
            'views',
            'comment_count',
            'comment_list',
            'image_url',
            'background_color',
            'color',
            'like_count',
            'is_liked',
            'created',
            'updated',
        )

    def get_like_count(self, obj):

        return Like.objects.filter(board_id=obj.id).count()

    def get_is_liked(self, obj):

        try:
            result = Like.objects.get(board_id = obj.id, user = obj.user)
        except Like.DoesNotExist:
            result = None
        return result is not None

    def get_comment_count(self, obj):

        return Comment.objects.filter(board_id=obj.id).count()

    def get_comment_list(self, obj):

        return Comment.objects.filter(board_id=obj.id)