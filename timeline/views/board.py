from rest_framework import generics

from ..models import Board, Like
from ..serializers import BoardSerializer

class BoardList(generics.ListCreateAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'timelie-board-list'

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'timeline-board-detail'

class BoardListByUser(generics.ListAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'timeline-board-list-by-user'

    def get_queryset(self):

        return Board.objects.filter(email = self.kwargs['user'])

class BoardListByLike(generics.ListAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'timeline-board-list-by-like'

    def get_queryset(self):

        like_result = Like.objects.filter(email = self.kwargs['user'])
        like_result = [like.board_id for like in like_result]
        return Board.objects.filter(id__in = like_result)
