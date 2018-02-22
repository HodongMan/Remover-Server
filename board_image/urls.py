from django.urls import path

from .views import (
    BoardImageList,
    BoardImageDetail,
)

urlpatterns = [
    path('', BoardImageList.as_view(), name = BoardImageList.name),
    path('<int:pk>/', BoardImageDetail.as_view(), name = BoardImageDetail.name),
]