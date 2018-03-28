from rest_framework import generics

from .serializers import UserInfoSerializer, UserSerializer
from .models import User
from board.models import Board, Like

class UserInfo(generics.RetrieveAPIView):

    serializer_class = UserInfoSerializer
    name = 'user-info'

    def get_object(self):

        like_count = Like.objects.raw("select * from board_like where board_like.board_id_id in (select id from board_board where user = %s)", [self.kwargs['user'],])
        like_count = (len(list(like_count)))
        board_count = Board.objects.filter(user_id=self.kwargs['user']).count()
        user_info = User.objects.get(user=self.kwargs['user'])
        return {
            "like_count" : like_count,
            "board_count" : board_count,
            "user" : user_info.user,
            "name" : user_info.name,
            "profile_image" : user_info.profile_image, 
        }

class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
