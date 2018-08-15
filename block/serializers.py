from rest_framework import serializers

from .models import BlockUser

class BlockUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = BlockUser
        fields = (
            'pk',
            'from_user',
            'to_user',
            'created',
            'updated',
        )