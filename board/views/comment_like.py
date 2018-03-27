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