from rest_framework import generics

from ..models import Comment
from ..serializers import CommentSerializer

class CommentList(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'

class CommentListByBoard(generics.ListAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list-by-board'

    def get_queryset(self):

        return Comment.objects.filter(board_id=self.kwargs['board'])