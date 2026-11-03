import unittest
from service.models import Product, db
from tests.factories import ProductFactory


class TestProductModel(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_read_a_product(self):
        product = ProductFactory()
        product.create()

        self.assertIsNotNone(product.id)

        found = Product.find(product.id)

        self.assertIsNotNone(found)
        self.assertEqual(found.id, product.id)
        self.assertEqual(found.name, product.name)
        self.assertEqual(found.description, product.description)
        self.assertEqual(found.price, product.price)

    def test_update_a_product(self):
        product = ProductFactory()
        product.create()

        original_id = product.id
        product.description = "Updated description"
        product.update()

        found = Product.find(original_id)

        self.assertEqual(found.id, original_id)
        self.assertEqual(found.description, "Updated description")

    def test_delete_a_product(self):
        product = ProductFactory()
        product.create()

        self.assertEqual(len(Product.all()), 1)

        product.delete()

        self.assertEqual(len(Product.all()), 0)
        self.assertIsNone(Product.find(product.id))

    def test_list_all_products(self):
        self.assertEqual(len(Product.all()), 0)

        ProductFactory.create_batch(5)

        products = Product.all()
        self.assertEqual(len(products), 5)

    def test_find_by_name(self):
        products = ProductFactory.create_batch(10)
        name = products[0].name

        expected_count = sum(1 for p in products if p.name == name)
        found = Product.find_by_name(name)

        self.assertEqual(len(found), expected_count)

        for product in found:
            self.assertEqual(product.name, name)

    def test_find_by_category(self):
        products = ProductFactory.create_batch(10)
        category = products[0].category

        expected_count = sum(1 for p in products if p.category == category)
        found = Product.find_by_category(category)

        self.assertEqual(len(found), expected_count)

        for product in found:
            self.assertEqual(product.category, category)

    def test_find_by_availability(self):
        products = ProductFactory.create_batch(10)
        available = products[0].available

        expected_count = sum(1 for p in products if p.available == available)
        found = Product.find_by_availability(available)

        self.assertEqual(len(found), expected_count)

        for product in found:
            self.assertEqual(product.available, available)
