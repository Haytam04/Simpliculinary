from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model=OrderItem
    extra=1
    fields=['product','quantity','price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemInline]
    fields=['user','status','shipping_adress']

#testing
