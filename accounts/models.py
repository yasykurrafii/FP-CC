from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(null = True, max_length=200)
    phone = models.CharField(null=True, max_length=200)
    email = models.CharField(null=True, max_length=200)
    date_created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(null = True, max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS = (
        ('Indoor', 'Indoor'),
        ('Out door', 'Out door')
    )
    name = models.CharField(null = True, max_length=200)
    price = models.FloatField(null = True)
    category = models.CharField(null = True, max_length=200, choices=STATUS)
    description = models.CharField(null = True, max_length=200, blank=True)
    date_created = models.DateTimeField(null=True, auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(null=True, auto_now_add=True)
    status = models.CharField(null=True, max_length=200, choices=STATUS)
    note = models.CharField(null = True, max_length=1000)

    def __str__(self):
        return self.product.name