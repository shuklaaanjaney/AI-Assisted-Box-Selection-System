from rest_framework.views import APIView
from rest_framework.response import Response

from boxes.models import Product
from .services import get_best_box


class RecommendationAPIView(APIView):

    def get(self, request, product_id):

        try:
            product = Product.objects.get(id=product_id)

        except Product.DoesNotExist:
            return Response({
                "error": "Product not found"
            }, status=404)

        box = get_best_box(product)

        if box is None:
            return Response({
                "message": "No suitable box found"
            })

        return Response({
            "product": product.name,
            "recommended_box": box.name,
            "cost": box.cost
        })
