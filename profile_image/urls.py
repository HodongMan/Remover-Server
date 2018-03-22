from django.urls import path

from .views import (
    ProfileImageList,
    ProfileImageDetail,
)

urlpatterns = [
    path('', ProfileImageList.as_view(), name = ProfileImageList.name),
    path('<int:pk>/', ProfileImageDetail.as_view(), name = ProfileImageDetail.name),
]