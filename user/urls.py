from django.urls import path

from .views import (
    UserInfo,
)

urlpatterns = [
    path('<str:user>/', UserInfo.as_view(), name = UserInfo.name),
]