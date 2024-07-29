from marshmallow import Schema, fields
from . import ma

class ShoppingCartSchema(ma.Schema):
    id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)

    class Meta:
        fields = ("id", "customer_id", "product_id", "quantity")

shopping_cart_schema = ShoppingCartSchema()
shopping_carts_schema = ShoppingCartSchema(many=True)