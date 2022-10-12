from django.contrib.auth.models import User
from rest_framework import viewsets, generics, views
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from backend.api.serializers import (
    ItemSerializer,
    CategorySerializer,
    CartSerializer,
    CartProductSerializer,
    CustomerSerializer, UserSerializer,
)
from backend.models import (
    Item,
    Category,
    Cart, CartProduct, Customer
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


class ItemDetailViewSet(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    lookup_field = 'name'
    queryset = Item.objects.all()


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class GetCustomerByToken(views.APIView):

    def get(self, request, key):
        token = Token.objects.filter(key=key).first()
        user = token.user
        customer = Customer.objects.filter(user=user).first()
        serializer = CustomerSerializer(customer, many=False)

        return Response(serializer.data)


class GetUserByToken(views.APIView):

    def get(self, request, key):
        token = Token.objects.filter(key=key).first()
        user = User.objects.filter(auth_token=token).first()
        serializer = UserSerializer(user, many=False)

        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
