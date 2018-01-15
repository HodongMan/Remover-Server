from rest_framework import serializers
from ..model import Board

class BoardSerializer(serializers.ModelSerializer):

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
            'created',
            'updated',
        )