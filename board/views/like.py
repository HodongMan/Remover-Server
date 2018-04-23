from rest_framework import generics

from ..models import Like
from ..serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    name = 'like-list'

class LikeDetail(generics.RetrieveAPIView):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    name = 'like-detail'

class LikeDestroyByUser(generics.DestroyAPIView):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    name = 'like-destroy-by-user'

    def get_object(self):

        like_result = Like.objects.get(user = self.kwargs['user'], board_id = self.kwargs['board'])
        return like_result