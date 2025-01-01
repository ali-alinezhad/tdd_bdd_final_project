import logging
from django.test import TestCase
from your_app.models import Product  # Replace `your_app` with the correct app name
from tests.factories import ProductFactory

logger = logging.getLogger("test")


class ProductModelTests(TestCase):
    def test_create_product(self):
        """Test creating a product"""
        product = ProductFactory()
        logger.debug("Created product: %s", product)
        self.assertIsNotNone(product.id)

    def test_read_product(self):
        """Test reading a product"""
        product = ProductFactory()
        logger.debug("Created product: %s", product)
        fetched_product = Product.objects.get(id=product.id)
        self.assertEqual(fetched_product.name, product.name)
        self.assertEqual(fetched_product.description, product.description)
        self.assertEqual(fetched_product.price, product.price)
        self.assertEqual(fetched_product.available, product.available)
        self.assertEqual(fetched_product.category, product.category)

    def test_update_product(self):
        """Test updating a product"""
        product = ProductFactory()
        logger.debug("Before update: %s", product)
        new_description = "Updated description"
        product.description = new_description
        product.save()
        updated_product = Product.objects.get(id=product.id)
        logger.debug("After update: %s", updated_product)
        self.assertEqual(updated_product.description, new_description)

    def test_delete_product(self):
        """Test deleting a product"""
        product = ProductFactory()
        logger.debug("Created product: %s", product)
        product_id = product.id
        product.delete()
        self.assertFalse(Product.objects.filter(id=product_id).exists())

    def test_list_all_products(self):
        """Test listing all products"""
        self.assertEqual(Product.objects.count(), 0)
        ProductFactory.create_batch(5)
        self.assertEqual(Product.objects.count(), 5)

    def test_find_product_by_name(self):
        """Test finding a product by name"""
        products = ProductFactory.create_batch(5)
        target_name = products[0].name
        found_products = Product.objects.filter(name=target_name)
        self.assertTrue(all(p.name == target_name for p in found_products))

    def test_find_product_by_availability(self):
        """Test finding a product by availability"""
        products = ProductFactory.create_batch(10)
        target_availability = products[0].available
        found_products = Product.objects.filter(available=target_availability)
        self.assertTrue(all(p.available == target_availability for p in found_products))

    def test_find_product_by_category(self):
        """Test finding a product by category"""
        products = ProductFactory.create_batch(10)
        target_category = products[0].category
        found_products = Product.objects.filter(category=target_category)
        self.assertTrue(all(p.category == target_category for p in found_products))
