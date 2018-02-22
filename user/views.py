from rest_framework import generics

from .serializers import UserInfoSerializer
from board.models import Board, Like

class UserInfo(generics.RetrieveAPIView):

    serializer_class = UserInfoSerializer
    name = 'user-info'

    def get_object(self):

        like_count = Like.objects.raw("select * from board_like where board_like.board_id_id in (select id from board_board where user = %s)", [self.kwargs['user'],])
        like_count = (len(list(like_count)))
        board_count = Board.objects.filter(user=self.kwargs['user']).count()
        return {
            "like_count" : like_count,
            "board_count" : board_count, 
        }
