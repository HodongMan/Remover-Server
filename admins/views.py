from django.db.models import Count
from rest_framework import generics

from board.models import Board, Like
from admins.serializers import NormalBoardSerializer
from block.models import BlockUser


class NormalBoardList(generics.ListCreateAPIView):

    queryset = Board.objects.all()
    serializer_class = NormalBoardSerializer
    name = 'normal-board-list'

class NormalBoardDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Board.objects.all()
    serializer_class = NormalBoardSerializer
    name = 'normal-board-detail'