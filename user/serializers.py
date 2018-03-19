from rest_framework import serializers

from .models import User
from board.models import Board, Like

class UserInfoSerializer(serializers.ModelSerializer):

    like_count = serializers.IntegerField()
    board_count = serializers.IntegerField()

    class Meta:

        model = User
        fields = (
            'user',
            'name',
            'profile_image',
            'like_count',
            'board_count'
        )

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = (
            'user',
            'name',
            'profile_image',
        )