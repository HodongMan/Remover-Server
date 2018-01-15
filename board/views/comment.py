from rest_framework import generics

from ..models import Comment
from ..serializers import CommentSerializer

class CommentList(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'

class commentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'
