from django.urls import path

from .views import CategoryList, CategoryDetail
from .views import BoardList, BoardDetail
from .views import CommentList, CommentDetail
from .views import LikeList, LikeDetail

urlpatterns = [
    path("category/", CategoryList.as_view(), name = CategoryList.name),
    path("category/<int:pk>/", CategoryDetail.as_view(), name = CategoryDetail.name),
    path("board/", BoardList.as_view(), name = BoardList.name),
    path("board/<int:pk>/", BoardDetail.as_view(), name = BoardDetail.name),
    path("comment/", CommentList.as_view(), name = CommentList.name),
    path("comment/<int:pk>/", CommentDetail.as_view(), name = CommentDetail.name),
    path("like/", LikeList.as_view(), name = LikeList.name),
    path("like/<int:pk>/", LikeDetail.as_view(), name = LikeDetail.name),
]