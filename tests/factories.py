import factory
from factory import Faker
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from your_app.models import Product  # Replace 'your_app' with the actual app name

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = Faker("word")
    description = Faker("sentence", nb_words=10)
    price = FuzzyDecimal(1.0, 100.0, precision=2)
    available = FuzzyChoice([True, False])
    category = FuzzyChoice(["Electronics", "Books", "Clothing", "Toys", "Furniture"])
