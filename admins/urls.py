from django.urls import path

from .views import ( 
    NormalBoardList, 
    NormalBoardDetail, 
    BoardDataCountView
)

urlpatterns = [
    path("board/", NormalBoardList.as_view(), name = NormalBoardList.name),
    path("board/<int:pk>/", NormalBoardDetail.as_view(), name = NormalBoardDetail.name),
    path("board/data/count", BoardDataCountView.as_view(), name = BoardDataCountView.name),
]