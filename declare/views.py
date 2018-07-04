from rest_framework import generics

from .models import Declare
from .serializers import DeclareSerializer

class DeclareList(generics.ListCreateAPIView):

    queryset = Declare.objects.all()
    serializer_class = DeclareSerializer
    name = 'declare-list'

class DeclareDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Declare.objects.all()
    serializer_class = DeclareSerializer
    name = 'declare-detail'