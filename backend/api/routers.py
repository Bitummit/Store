from rest_framework import routers

from backend.api.api_views import (
    ItemsViewSet,
    CategoryViewSet,
    CartViewSet,
    CustomerViewSet,
    CartProductViewSet,
    UserViewSet
)

router = routers.DefaultRouter()
router.register("items", ItemsViewSet)
router.register("category", CategoryViewSet)
router.register("cart", CartViewSet)
router.register("cartProduct", CartProductViewSet)
router.register("customer", CustomerViewSet)
router.register("my_users", UserViewSet)
