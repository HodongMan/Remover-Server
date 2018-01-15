from django.urls import path

from .views import BoardList, BoardDetail
from .views import CommentList, CommentDetail
from .views import LikeList, LikeDetail

urlpatterns = [
    path('board/', BoardList.as_view(), name = BoardList.name),
    path('board/<int:pk>/', BoardDetail.as_view(), name = BoardDetail.name),
    path('comment/', CommentList.as_view(), name = CommentList.name),
    path('comment/<int:pk>/', CommentDetail.as_view(), name = CommentDetail.name),
    path('like/', LikeList.as_view(), name = LikeList.name),
    path('like/<int:pl>/', LikeDetail.as_view(), name = LikeDetail.name),
]