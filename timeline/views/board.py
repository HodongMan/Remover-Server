from rest_framework import generics

from ..models import Board
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

        return Board.objects.filter(user=self.kwargs['user'])

class BoardListByCategory(generics.ListAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'timeline-board-list-by-category'

    def get_queryset(self):

        return Board.objects.filter(category=self.kwargs['category'])