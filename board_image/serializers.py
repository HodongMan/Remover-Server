from rest_framework import serializers
from .models import BoardImage

class BoardImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = BoardImage
        fields = (
            'pk',
            'image_url',
            'font_color',
        )

