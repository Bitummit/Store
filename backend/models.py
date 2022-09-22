from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Material(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Size(models.Model):
    size = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.size}"


class Item(models.Model):
    name = models.CharField(max_length=128)
    material = models.ManyToManyField(Material, related_name='items')
    desc = models.TextField()
    sizes_in_stock = models.ManyToManyField(Size, related_name='items')
    price = models.DecimalField(decimal_places=2, max_digits=8)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"Item {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Category {self.name}"


class Cart(models.Model):
    items = models.ManyToManyField('CartProduct', related_name='cart')
    owner = models.ForeignKey('Customer', on_delete=models.CASCADE)
    final_price = models.DecimalField(decimal_places=2, max_digits=9)
    total_items = models.IntegerField()

    def __str__(self):
        return f"User's {self.owner} cart"


class CartProduct(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.CharField(max_length=16)
    qty = models.IntegerField()
    final_price = models.DecimalField(decimal_places=2, max_digits=9)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField('Order', blank=True, related_name="customer")
    phone = models.CharField(max_length=20, verbose_name="Телeфон")
    address = models.CharField(max_length=1024, null=True, blank=True)


class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = "is_ready"
    STATUS_COMPLETED = "completed"

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ получен покупателем')
    )

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_NEW)
    address = models.CharField(max_length=256)
    comment = models.TextField()
    created_at = models.DateField(auto_now=True)
    completed_at = models.DateField(default=timezone.now)
