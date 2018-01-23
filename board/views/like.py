from rest_framework import generics

from ..models import Like
from ..serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    name = 'like-list'

class LikeDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    name = 'like-detail'