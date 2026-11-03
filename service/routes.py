from flask import jsonify, request
from service import app
from service.models import Product


# READ a Product
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.find(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product.serialize()), 200


# UPDATE a Product
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.find(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json()
    product.deserialize(data)
    product.update()

    return jsonify(product.serialize()), 200


# DELETE a Product
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.find(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    product.delete()
    return "", 204


# LIST ALL / SEARCH Products
@app.route("/products", methods=["GET"])
def list_products():
    products = Product.all()

    name = request.args.get("name")
    category = request.args.get("category")
    availability = request.args.get("availability")

    if name:
        products = Product.find_by_name(name)

    if category:
        products = [
            product for product in products
            if product.category == category
        ]

    if availability is not None:
        is_available = availability.lower() == "true"
        products = [
            product for product in products
            if product.availability == is_available
        ]

    return jsonify([product.serialize() for product in products]), 200
