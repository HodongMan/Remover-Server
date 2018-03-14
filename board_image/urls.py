from django.urls import path

from .views import (
    BoardImageList,
    BoardImageDetail,
    BoardImageRandomList,
)

urlpatterns = [
    path('', BoardImageList.as_view(), name = BoardImageList.name),
    path('<int:pk>/', BoardImageDetail.as_view(), name = BoardImageDetail.name),
    path('random/', BoardImageRandomList.as_view(), name = BoardImageRandomList.name),
]