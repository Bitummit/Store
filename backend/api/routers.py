from rest_framework import routers

from backend.api.api_views import (
    ItemsViewSet,
    CategoryViewSet,
    CartViewSet,
    CustomerViewSet,
    CartProductViewSet
)

router = routers.DefaultRouter()
router.register("items", ItemsViewSet)
router.register("category", CategoryViewSet)
router.register("cart", CartViewSet)
router.register("cartProduct", CartProductViewSet)
router.register("customer", CustomerViewSet)
