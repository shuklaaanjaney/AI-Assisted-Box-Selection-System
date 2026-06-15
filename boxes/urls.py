from django.urls import path
from .views import (ProductListCreateAPIView, BoxListCreateAPIView, OrderListCreateAPIView)

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view()),
    path('boxes/', BoxListCreateAPIView.as_view()),
    path('orders/', OrderListCreateAPIView.as_view()),
]