from django.test import TestCase
from rest_framework.test import APITestCase

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

        Box.objects.create(
            name="Small Box",
            length=35,
            width=25,
            height=10,
            max_weight=5,
            cost=50
        )

        Box.objects.create(
            name="Medium Box",
            length=50,
            width=40,
            height=20,
            max_weight=10,
            cost=80
        )

    def test_no_suitable_box_found(self):

        oversized_product = Product.objects.create(
            name="Industrial Machine",
            length=500,
            width=500,
            height=500,
            weight=100
        )

        recommended_box = get_best_box(
            oversized_product
        )

        self.assertIsNone(
            recommended_box
        )

    def test_cheapest_box_is_selected(self):

        Box.objects.create(
            name="Cheap Box",
            length=40,
            width=30,
            height=15,
            max_weight=5,
            cost=30
        )

        recommended_box = get_best_box(
            self.product
        )

        self.assertEqual(
            recommended_box.name,
            "Cheap Box"
        )

    def test_box_selection_with_rotation(self):

        product = Product.objects.create(
            name="Monitor",
            length=30,
            width=20,
            height=10,
            weight=3
        )

        Box.objects.create(
            name="Rotated Box",
            length=20,
            width=30,
            height=10,
            max_weight=5,
            cost=40
        )

        recommended_box = get_best_box(product)
        self.assertEqual(recommended_box.name,"Rotated Box")

    def test_product_exceeds_weight_limit(self):

        heavy_product = Product.objects.create(
            name="Heavy Machine",
            length=20,
            width=20,
            height=20,
            weight=20
        )
        recommended_box = get_best_box(heavy_product)
        self.assertIsNone(recommended_box)


class RecommendationAPITest(APITestCase):

    def setUp(self):

        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        Box.objects.create(
            name="Small Box",
            length=35,
            width=25,
            height=10,
            max_weight=5,
            cost=50
        )

    def test_recommendation_endpoint(self):
        response = self.client.get(f"/api/recommendation/{self.product.id}/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["recommended_box"],"Small Box")      