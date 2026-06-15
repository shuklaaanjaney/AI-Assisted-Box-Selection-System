from rest_framework import serializers
from .models import Product, Box, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'