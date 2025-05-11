from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model=OrderItem
    extra=1
    fields=['product','quantity','show_price']
    readonly_fields = ['show_price'] 

    def show_price(self,obj):
        return f'{obj.product_price} DH'
    show_price.short_description='Product Price'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemInline]
    fields=['user','status','shipping_adress']
