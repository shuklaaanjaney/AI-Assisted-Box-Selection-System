from django.test import TestCase
from django.core.exceptions import ValidationError

from boxes.models import Product, Box
from recommendation.services import get_best_box


class ProductAndBoxTests(TestCase):

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

    def test_negative_product_dimensions_not_allowed(self):

        product = Product(
            name="Invalid Product",
            length=-10,
            width=20,
            height=5,
            weight=1
        )

        with self.assertRaises(
            ValidationError
        ):
            product.full_clean()

    def test_negative_box_dimensions_not_allowed(self):

        box = Box(
            name="Invalid Box",
            length=-10,
            width=20,
            height=10,
            max_weight=5,
            cost=50
        )

        with self.assertRaises(
            ValidationError
        ):
            box.full_clean()
