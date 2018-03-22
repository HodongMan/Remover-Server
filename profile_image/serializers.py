from rest_framework import serializers
from .models import ProfileImage

class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProfileImage
        fields = (
            'pk',
            'image_url',
        )

