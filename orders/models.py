from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Regular_Pizza(models.Model):
    name = models.CharField(max_length=50)
    small = models.DecimalField(max_digits=6, decimal_places=2)
    large = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class Sicilian_Pizza(models.Model):
    name = models.CharField(max_length=50)
    small = models.DecimalField(max_digits=6, decimal_places=2)
    large = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Sub(models.Model):
    name = models.CharField(max_length=50)
    small = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    large = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class Dinner_Platter(models.Model):
    name = models.CharField(max_length=50)
    small = models.DecimalField(max_digits=6, decimal_places=2)
    large = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class Pasta(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class Salad(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    name = models.CharField(max_length=50)
    typeof = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField()
    topping1 = models.CharField(max_length=50, null=True, blank=True)
    topping2 = models.CharField(max_length=50, null=True, blank=True)
    topping3 = models.CharField(max_length=50, null=True, blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=50)
    orderedby = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"Order No.{self.id} by {self.orderedby}"


class Placed_Order(models.Model):
    detail = models.TextField()
    orderedby = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    status = models.CharField(max_length=50)
    totalprice = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Order No.{self.id} by {self.orderedby}"


class AddOn(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name}"
