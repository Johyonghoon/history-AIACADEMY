from django.db import models
from django.utils import timezone

from shop.deliveries.models import Delivery
from shop.products.models import Product
from shop.shop_users.models import ShopUser


class Order(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    delivery_id = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    class Meta:
        db_table = "shop_orders"

    def __str__(self):
        return f"{self.pk} {self.created_at} {self.product_id} {self.user_id} {self.delivery_id}"
