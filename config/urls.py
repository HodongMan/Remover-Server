from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/user/', include('user.urls')),
    path('api/timeline/', include('timeline.urls')),
    path('api/board/', include('board.urls')),
]
