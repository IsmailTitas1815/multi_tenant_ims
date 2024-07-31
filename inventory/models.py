# inventory/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
