from django.contrib import admin
from .models import (
    Cart,
    CartProduct,
    Item,
    Category,
    Order,
    Customer,
    Material,
    Size
)

admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Material)
admin.site.register(Size)
