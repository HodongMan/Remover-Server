from django.shortcuts import render
from rest_framework import generics

from .models import BlackList
from .serializers import BlackListSerializer

class BlackLists(generics.ListCreateAPIView):

    queryset = BlackList.objects.all()
    serializer_class = BlackListSerializer
    name = 'black-lists'

class BlackListDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = BlackList.objects.all()
    serializer_class = BlackListSerializer
    name = 'black-list-detail'
