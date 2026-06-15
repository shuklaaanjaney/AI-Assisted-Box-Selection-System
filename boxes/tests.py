from django.test import TestCase
from boxes.models import Product, Box
from recommendation.services import get_best_box


class RecommendationTests(TestCase):

    def setUp(self):

        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        self.small_box = Box.objects.create(
            name="Small Box",
            length=35,
            width=25,
            height=10,
            max_weight=5,
            cost=50
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            length=50,
            width=40,
            height=20,
            max_weight=10,
            cost=80
        )

    def test_product_created(self):
        self.assertEqual(self.product.name,"Laptop")

    def test_recommendation_returns_small_box(self):
        recommended_box = get_best_box(self.product)
        self.assertEqual(recommended_box.name,"Small Box")
