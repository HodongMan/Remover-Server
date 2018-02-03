from rest_framework import serializers
from ..models import Board, Like

class BoardSerializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()

    class Meta:

        model = Board
        fields = (
            'id',
            'category_id',
            'email',
            'name',
            'title',
            'description',
            'views',
            'image_url',
            'background_color',
            'color',
            'like_count',
            'created',
            'updated',
        )

    def get_like_count(self, obj):

        return Like.objects.filter(board_id=obj.id).count()