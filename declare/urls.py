from django.urls import path

from .views import (
    DeclareList,
    DeclareDetail
)

urlpatterns = [
    path('', DeclareList.as_view(), name=DeclareList.name),
    path('<int:pk>/', DeclareDetail.as_view(), name=DeclareDetail.name),
]