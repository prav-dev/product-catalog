import unittest
from service import app, db
from tests.factories import ProductFactory


class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        self.client = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_read_a_product(self):
        product = ProductFactory()
        product.create()

        response = self.client.get(f"/products/{product.id}")

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], product.id)
        self.assertEqual(data["name"], product.name)

    def test_update_a_product(self):
        product = ProductFactory()
        response = self.client.post("/products", json=product.serialize())
        self.assertEqual(response.status_code, 201)

        product_id = response.get_json()["id"]

        response = self.client.put(
            f"/products/{product_id}",
            json={"description": "Updated product description"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["description"],
            "Updated product description"
        )

    def test_delete_a_product(self):
        product = ProductFactory()
        product.create()

        initial_count = len(ProductFactory._meta.model.all())

        response = self.client.delete(f"/products/{product.id}")

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, b"")

        final_count = len(ProductFactory._meta.model.all())
        self.assertEqual(final_count, initial_count - 1)

        response = self.client.get(f"/products/{product.id}")
        self.assertEqual(response.status_code, 404)

    def test_list_all_products(self):
        ProductFactory.create_batch(5)

        response = self.client.get("/products")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 5)

    def test_list_products_by_name(self):
        product = ProductFactory()
        product.name = "Laptop"
        product.create()

        response = self.client.get("/products?name=Laptop")

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Laptop")

    def test_list_products_by_category(self):
        product = ProductFactory()
        product.category = "Electronics"
        product.create()

        response = self.client.get("/products?category=Electronics")

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["category"], "Electronics")

    def test_list_products_by_availability(self):
        product = ProductFactory()
        product.available = True
        product.create()

        response = self.client.get("/products?availability=true")

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertTrue(data[0]["availability"])
