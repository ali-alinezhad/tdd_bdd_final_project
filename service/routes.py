from flask import jsonify, abort
from service.models import Product
from service.common.status import HTTP_200_OK, HTTP_404_NOT_FOUND

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """
    Retrieve a single Product by its ID
    """
    product = Product.find(product_id)
    if not product:
        abort(HTTP_404_NOT_FOUND, description=f"Product with id {product_id} was not found.")
    return jsonify(product.serialize()), HTTP_200_OK
