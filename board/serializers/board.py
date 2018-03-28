from rest_framework import serializers

from ..models import Board, Comment, Like
from user.models import User
from user.serializers import UserSerializer

class BoardSerializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    user_id = UserSerializer(read_only=True)
    
    class Meta:

        model = Board
        fields = (
            'id',
            'category_id',
            'description',
            'user_id',
            'views',
            'comment_count',
            'image_url',
            'background_color',
            'color',
            'like_count',
            'is_liked',
            'created',
            'updated',
        )

    def create(self, validated_data):
        
        user = self.context['request'].query_params['user']
        validated_data['user_id'] = User.objects.get(user=user)
        return Board.objects.create(**validated_data)
     

    def get_like_count(self, obj):

        return Like.objects.filter(board_id=obj.id).count()

    def get_is_liked(self, obj):

        request = self.context['request']
        
        try:
            user = request.query_params['user']
            result = Like.objects.get(board_id = obj.id, user = user)
        except:
            result = None
        return result is not None

    def get_comment_count(self, obj):

        return Comment.objects.filter(board_id=obj.id).count()