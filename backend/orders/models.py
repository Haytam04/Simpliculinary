from django.db import models
from users.models import CustomUser
from decimal import Decimal
from products.models import Product

class Order(models.Model):
    status_choice=[
        ('Pending', 'Pending'),
        ('Payed', 'Payed'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ]

    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders', verbose_name='client')
    total= models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('0.00'))
    status= models.CharField(max_length=250, choices=status_choice, default='Pending')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")
    shipping_adress= models.TextField()    

    def __str__(self):
        return f'Commande N {self.id} -- Client {self.user.username}'
    

class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item')
    quantity= models.PositiveIntegerField(default=0)
    price= models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))

    @property
    def product_price(self):
        return self.product.price
    def __str__(self):
        return f'{self.quantity} unité(s) du {self.product.name}'
