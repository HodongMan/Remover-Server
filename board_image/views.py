from random import shuffle, sample
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

class BoardImageRandomList(generics.ListAPIView):

    queryset = BoardImage.objects.all()
    serializer_class = BoardImageSerializer
    name = 'board-image-random-list'

    def get_queryset(self):

        board_image_list = list(BoardImage.objects.all())
        shuffle(board_image_list)
        return board_image_list