from rest_framework import viewsets

from backend.api.serializers import (
    ItemSerializer,
    CategorySerializer
)
from backend.models import (
    Item,
    Category
)


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

