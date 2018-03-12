from rest_framework import serializers

from ..models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = (
            'id',
            'title',
            'image_url',
            'background_url',
            'color',
            'banner',
            'created',
        )