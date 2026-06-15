from django.urls import path
from .views import RecommendationAPIView

urlpatterns = [
    path('<int:product_id>/', RecommendationAPIView.as_view()),
]