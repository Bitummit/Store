from rest_framework import viewsets, generics

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


class FilterItemsViewSet(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        items = Item.objects.all()
        category_name = self.kwargs.get('name', '')
        print(category_name)
        if category_name:
            category = Category.objects.filter(name=category_name).first()
            items = items.filter(category=category)

        return items


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



