from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/user/', include('user.urls')),
    path('api/timeline/', include('timeline.urls')),
    path('api/board/', include('board.urls')),
    path('api/boardimage/', include('board_image.urls')),
] + static(settings.STATIC_URL)
