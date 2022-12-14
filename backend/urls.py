from django.urls import path, include
from backend.api.api_views import (
    FilterItemsViewSet,
    ItemDetailViewSet,
    GetCustomerByToken,
    GetUserByToken,
    GetCartByCustomer
)
from backend.api.routers import router

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),

    path('api/items/by/category/<str:name>/', FilterItemsViewSet.as_view()),
    path('api/items/detail/<str:name>/', ItemDetailViewSet.as_view()),
    path('api/customer/profile/<str:key>/', GetCustomerByToken.as_view()),
    path('api/user/by/token/<str:key>/', GetUserByToken.as_view()),
    path('api/cart/by/customer/<int:customer_id>/', GetCartByCustomer.as_view()),
]
