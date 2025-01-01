from behave import given
from service.models import db, Product

@given('the following products exist')
def step_impl(context):
    """
    Load products from the context.table into the database.
    """
    db.session.query(Product).delete()  # Clear existing products
    db.session.commit()

    for row in context.table:
        product = Product(
            id=int(row["id"]),
            name=row["name"],
            description=row["description"],
            price=float(row["price"]),
            available=row["available"].lower() == "true",
            category=row["category"],
        )
        db.session.add(product)
    db.session.commit()
