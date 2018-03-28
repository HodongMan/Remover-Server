from django.urls import path

from .views import (
    UserInfo,
    UserList,
    UserDetail,
)

urlpatterns = [
    path('', UserList.as_view(), name = UserList.name),
    path('<str:pk>/', UserDetail.as_view(), name = UserDetail.name),
    path('info/<str:user>/', UserInfo.as_view(), name = UserInfo.name),
]