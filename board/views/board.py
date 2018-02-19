from rest_framework import generics

from ..models import Board, Like
from ..serializers import BoardSerializer

class BoardList(generics.ListCreateAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-list'

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-detail'

class BoardListByUser(generics.ListAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-list-by-user'

    def get_queryset(self):

        return Board.objects.filter(user=self.kwargs['user'])

class BoardListByCategory(generics.ListAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-list-by-category'

    def get_queryset(self):

        return Board.objects.filter(category_id=self.kwargs['category'])

class BoardListByLike(generics.ListAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-list-by-like'

    def get_queryset(self):

        like_result = Like.objects.filter(user = self.kwargs['user'])
        like_result = [like.board_id for like in like_result]
        return Board.objects.filter(id__in = like_result)