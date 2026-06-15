from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()

    def volume(self):
        return self.length * self.width * self.height

    
    def __str__(self):
        return self.name    


class Box(models.Model):
    name = models.CharField(max_length=255)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    max_weight = models.FloatField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def volume(self):
        return self.length * self.width * self.height

    def __str__(self):
        return self.name    


class Order(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    selected_box = models.ForeignKey(
        Box,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )