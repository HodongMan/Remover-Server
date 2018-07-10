from rest_framework import serializers

from .models import BlackList

class BlackListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlackList
        fields = (
            'id',
            'user',
            'created',
        )