from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):

    name = models.CharField(
        max_length=255
    )

    length = models.FloatField(
        validators=[
            MinValueValidator(0.01)
        ]
    )

    width = models.FloatField(
        validators=[
            MinValueValidator(0.01)
        ]
    )

    height = models.FloatField(
        validators=[
            MinValueValidator(0.01)
        ]
    )

    weight = models.FloatField(
        validators=[
            MinValueValidator(0.01)
        ]
    )

    def volume(self):
        return (
            self.length *
            self.width *
            self.height
        )

    def __str__(self):
        return self.name


class Box(models.Model):

    name = models.CharField(
        max_length=255
    )

    length = models.FloatField(
        validators=[
            MinValueValidator(0.01)
        ]
    )

    width = models.FloatField(
        validators=[
            MinValueValidator(0.01)
        ]
    )

    height = models.FloatField(
        validators=[
            MinValueValidator(0.01)
        ]
    )

    max_weight = models.FloatField(
        validators=[
            MinValueValidator(0.01)
        ]
    )

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01)
        ]
    )

    def volume(self):
        return (
            self.length *
            self.width *
            self.height
        )

    def __str__(self):
        return self.name


class Order(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    selected_box = models.ForeignKey(Box, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Order #{self.id}")