
from django.urls import path, include
from backend.api.api_views import FilterItemsViewSet
from backend.api.routers import router

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/items/by/category/<str:name>/', FilterItemsViewSet.as_view()),
]
