from rest_framework import serializers

from ..models import Board, Like

class BoardSerializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        
        model = Board
        fields = (
            'pk',
            'user',
            'name',
            'description',
            'views',
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