from rest_framework import generics

from .models import BlockUser
from .serializers import BlockUserSerializer

class BlockUserList(generics.ListCreateAPIView):

    queryset = BlockUser.objects.all()
    serializer_class = BlockUserSerializer
    name = 'block-user-list'

class BlockUserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = BlockUser.objects.all()
    serializer_class = BlockUserSerializer
    name = 'block-user-detail'

class BlockUserListByUser(generics.ListAPIView):

    queryset = BlockUser.objects.all()
    serializer_class = BlockUserSerializer
    name = 'block-user--list-by-user'

    def get_queryset(self):

        return BlockUser.objects.filter(from_user=self.kwargs['user']).order_by('-id')