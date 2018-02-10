from django.urls import path

from .views import (
    BoardList, 
    BoardDetail,
    BoardListByUser,
)
from .views import CommentList, CommentDetail
from .views import LikeList, LikeDetail

urlpatterns = [
    path('', BoardList.as_view(), name = BoardList.name),
    path('<int:pk>/', BoardDetail.as_view(), name = BoardDetail.name),
    path("search/user/<str:user>/", BoardListByUser.as_view(), name = BoardListByUser.name),
    path('comment/', CommentList.as_view(), name = CommentList.name),
    path('comment/<int:pk>/', CommentDetail.as_view(), name = CommentDetail.name),
    path('like/', LikeList.as_view(), name = LikeList.name),
    path('like/<int:pk>/', LikeDetail.as_view(), name = LikeDetail.name),
]