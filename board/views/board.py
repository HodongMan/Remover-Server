from django.db.models import Count
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

    def get_object(self):

        result = Board.objects.get(pk=self.kwargs['pk'])
        result.views += 1
        result.save()

        return result

class BoardListByUser(generics.ListAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-list-by-user'

    def get_queryset(self):

        return Board.objects.filter(user_id=self.kwargs['user'])

class BoardListByLikeCount(generics.ListAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-list-by-like-count'

    def get_queryset(self):

        queryset = Board.objects.raw("select * from board_board order by (select count(*) from board_like where board_board.id = board_like.board_id_id) desc;")
        return list(queryset)

class BoardListByCategoryAndLikeCount(generics.ListAPIView):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'board-list-by-category-and-like-count'

    def get_queryset(self):

        queryset = Board.objects.raw("select * from board_board where board_board.category_id_id = %sorder by (select count(*) from board_like where board_board.id = board_like.board_id_id) desc;", self.kwargs['category'])
        return list(queryset)



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