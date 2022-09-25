from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from rest_framework.authtoken import views

from Store import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('api-token-auth/', views.obtain_auth_token),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
