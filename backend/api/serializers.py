from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from backend.models import Item, Category, Material, Size, Cart, CartProduct, Customer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = 'name'


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = 'size'


class ItemSerializer(serializers.ModelSerializer):
    material = serializers.StringRelatedField(many=True)
    sizes_in_stock = serializers.StringRelatedField(many=True)

    class Meta:
        model = Item
        fields = '__all__'


class CartProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartProduct
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cart
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CustomerSerializer(serializers.ModelSerializer):
    orders = serializers.StringRelatedField(many=True)
    user = UserSerializer

    class Meta:
        model = Customer
        fields = '__all__'


