from django.urls import path

from .views import CategoryList, CategoryDetail
from .views import (
    BoardList, 
    BoardDetail,
    BoardListByUser,
    BoardListByLike,
    BoardListByCategory,
    BoardListByLikeCount,
)
from .views import CommentList, CommentDetail
from .views import LikeList, LikeDetail

urlpatterns = [
    path("", BoardList.as_view(), name = BoardList.name),
    path("<int:pk>/", BoardDetail.as_view(), name = BoardDetail.name),
    path("favorite/", BoardListByLikeCount.as_view(), name = BoardListByLikeCount.name),
    path("search/category/<str:category>/", BoardListByCategory.as_view(), name = BoardListByCategory.name),
    path("search/user/<str:user>/", BoardListByUser.as_view(), name = BoardListByUser.name),
    path('user/like/<str:user>/', BoardListByLike.as_view(), name = BoardListByLike.name),
    path("category/", CategoryList.as_view(), name = CategoryList.name),
    path("category/<int:pk>/", CategoryDetail.as_view(), name = CategoryDetail.name),
    path("comment/", CommentList.as_view(), name = CommentList.name),
    path("comment/<int:pk>/", CommentDetail.as_view(), name = CommentDetail.name),
    path("like/", LikeList.as_view(), name = LikeList.name),
    path("like/<int:pk>/", LikeDetail.as_view(), name = LikeDetail.name),
]