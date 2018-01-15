from rest_framework import serializers

from ..models import Board

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Board
        fields = (
            'pk',
            'email',
            'name',
            'title',
            'description',
            'vies',
            'image_url',
            'background_color',
            'color',

            'created',
            'updated',
        )