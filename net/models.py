from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_model = models.CharField(max_length=100)
    product_launch_date = models.DateField(auto_now=False)


class Network(models.Model):
    type = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    employees = models.CharField(max_length=200)
    debt = models.FloatField(null=True)
    products = models.ManyToManyField(Product)
    pub_date = models.DateTimeField('date published')
