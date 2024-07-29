from flask import Blueprint, request
from controllers.shoppingCartController import add_product_to_cart, remove_product_from_cart, get_cart_items

shopping_cart_blueprint = Blueprint('shopping_cart', __name__)


shopping_cart_blueprint.route("/add", methods=["POST"])(add_product_to_cart)
shopping_cart_blueprint.route("/remove", methods=["POST"])(remove_product_from_cart)
shopping_cart_blueprint.route("/<int:customer_id>", methods=["GET"])(get_cart_items)