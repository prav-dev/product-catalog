import requests
from behave import given


@given('the following products')
def step_impl(context):
    for row in context.table:
        payload = {
            "name": row["name"],
            "description": row["description"],
            "price": float(row["price"]),
            "available": row["available"].lower() == "true",
            "category": row["category"]
        }

        response = requests.post(
            "http://localhost:5000/products",
            json=payload
        )

        assert response.status_code == 201
