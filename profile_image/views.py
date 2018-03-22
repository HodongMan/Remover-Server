from rest_framework import generics

from .models import ProfileImage
from .serializers import ProfileImageSerializer


class ProfileImageList(generics.ListCreateAPIView):

    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer
    name = 'profile-image-list'

class ProfileImageDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer
    name = 'profile-image-detail'