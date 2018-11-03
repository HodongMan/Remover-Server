from rest_framework import serializers

from board.models import Board, Comment, Like
from user.models import User
from user.serializers import UserSerializer

class NormalBoardSerializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    
    class Meta:

        model = Board
        fields = (
            'id',
            'category_id',
            'user_id',
            'description',
            'views',
            'comment_count',
            'image_url',
            'background_color',
            'color',
            'like_count',
            'created',
            'updated',
        )
    
    def get_like_count(self, obj):

        return Like.objects.filter(board_id=obj.id).count()

    def get_comment_count(self, obj):

        return Comment.objects.filter(board_id=obj.id).count()


class BoardDataCountSerializer(serializers.Serializer):

    board_count = serializers.IntegerField()
    comment_count = serializers.IntegerField()
    last_month_board_count = serializers.IntegerField()
    last_day_board_count = serializers.IntegerField()