from django.db import models
from users.models import CustomUser
from products.models import Product

class Cart(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cart', verbose_name='client')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")

    def __str__(self):
        return f'Panier de {self.user.username}'
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_item')  
    quantity=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.quantity} unité(s) du {self.product.name}'