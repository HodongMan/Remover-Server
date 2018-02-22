from rest_framework import serializers

from board.models import Board, Like

class UserInfoSerializer(serializers.Serializer):

    like_count = serializers.IntegerField()
    board_count = serializers.IntegerField()

