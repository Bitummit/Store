from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

from Store import settings
from backend.api.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
