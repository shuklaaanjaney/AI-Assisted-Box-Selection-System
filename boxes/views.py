from rest_framework import generics
from .models import Product, Box, Order
from .serializers import (ProductSerializer, BoxSerializer, OrderSerializer)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BoxListCreateAPIView(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
