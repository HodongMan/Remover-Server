from django.urls import path

from .views import (
    BlackLists,
    BlackListDetail
)

urlpatterns = [
    path('', BlackLists.as_view(), name = BlackLists.name),
    path('<int:pk>/', BlackListDetail.as_view(), name = BlackListDetail.name),
]