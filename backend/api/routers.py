from rest_framework import routers

from backend.api.api_views import ItemsViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register("items", ItemsViewSet)
router.register("category", CategoryViewSet)
