from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250,verbose_name='product name ')
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True,upload_to='./products')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='products')

    def __str__(self):
        return f'{self.name} -- {self.category.name}'