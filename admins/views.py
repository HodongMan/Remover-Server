from django.db.models import Count
from rest_framework import generics

from board.models import Board, Comment, Like
from admins.serializers import NormalBoardSerializer, BoardDataCountSerializer
from block.models import BlockUser


class NormalBoardList(generics.ListCreateAPIView):

    queryset = Board.objects.all()
    serializer_class = NormalBoardSerializer
    name = 'normal-board-list'

class NormalBoardDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Board.objects.all()
    serializer_class = NormalBoardSerializer
    name = 'normal-board-detail'

class BoardDataCountView(generics.RetrieveAPIView):

    serializer_class = BoardDataCountSerializer
    name = 'board-data-count'

    def get_object(self):

        board_count = Board.objects.all().count()
        comment_count = Comment.objects.all().count()
        last_month_board_count = 0
        last_day_board_count = 0
        
        return {
            "board_count" : board_count,
            "comment_count" : comment_count,
            "last_month_board_count" : last_month_board_count,
            "last_day_board_count" : last_day_board_count, 
        }
