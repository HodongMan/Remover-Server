from rest_framework import generics

from ..models import CommentLike
from ..serializers import CommentLikeSerializer

class CommentLikeList(generics.ListCreateAPIView):

    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    name = 'comment-like-list'

class CommentLikeDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    name = 'comment-like-detail'

class CommentLikeDestroyByUser(generics.DestroyAPIView):

    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    name = 'comment-like-destroy-by-user'

    def get_object(self):

        like_result = CommentLike.objects.get(user = self.kwargs['user'], comment_id = self.kwargs['comment'])
        return like_result