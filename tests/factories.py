import factory
from factory.faker import Faker
from service.models import Product


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n + 1)
    name = Faker("name")
    description = Faker("text")
    price = Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    available = Faker("boolean")
    category = Faker("word")
