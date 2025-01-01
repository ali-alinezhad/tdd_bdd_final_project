import unittest
from flask import json
from service.models import db
from service.routes import app
from tests.factories import ProductFactory

BASE_URL = "/products"

class TestProductRoutes(unittest.TestCase):
    """Test Cases for Product Routes"""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        app.testing = True
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests"""
        db.session.close()

    def _create_products(self, count):
        """Helper method to create products in bulk"""
        products = []
        for _ in range(count):
            product = ProductFactory()
            products.append(product)
            db.session.add(product)
        db.session.commit()
        return products

    def test_get_product(self):
        """Test getting a single product"""
        test_product = self._create_products(1)[0]
        response = self.client.get(f"{BASE_URL}/{test_product.id}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], test_product.id)
        self.assertEqual(data["name"], test_product.name)
        self.assertEqual(data["description"], test_product.description)
        self.assertEqual(data["price"], test_product.price)
        self.assertEqual(data["available"], test_product.available)
        self.assertEqual(data["category"], test_product.category)

    def test_get_product_not_found(self):
        """Test getting a product that does not exist"""
        response = self.client.get(f"{BASE_URL}/0")
        self.assertEqual(response.status_code, 404)
