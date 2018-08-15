from django.urls import path

from .views import (
    BlockUserList,
    BlockUserDetail,
    BlockUserListByUser,
)

urlpatterns = [
    path("user", BlockUserList.as_view(), name = BlockUserList.name),
    path("user/<int:pk>/", BlockUserDetail.as_view(), name = BlockUserDetail.name),
    path("user/<str:user>/", BlockUserListByUser.as_view(), name = BlockUserListByUser.name),
]