from rest_framework import generics

from .models import BoardImage
from .serializers import BoardImageSerializer


class BoardImageList(generics.ListCreateAPIView):

    queryset = BoardImage.objects.all()
    serializer_class = BoardImageSerializer
    name = 'board-image-list'

class BoardImageDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = BoardImage.objects.all()
    serializer_class = BoardImageSerializer
    name = 'board-image-detail'
