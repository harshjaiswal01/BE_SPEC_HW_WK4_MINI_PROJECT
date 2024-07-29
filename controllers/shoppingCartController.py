from services import shoppingCart
from database import db #need db be to serve incoming data to db
from models.customer import Customer #need this to creat Customer Objects
from sqlalchemy import select, delete, func
from marshmallow import fields, ValidationError
from flask import Flask, jsonify, request
from utils.util import admin_required, token_required
from models.schemas.shoppingcart import shopping_cart_schema

@token_required
def add_product_to_cart():
    data = request.get_json()
    print("Data: ", data)
    customer_id = data.get('customer_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    cart = shoppingCart.add_product_to_cart(customer_id, product_id, quantity)
    print(cart)
    return cart

@token_required
def remove_product_from_cart():
    data = request.get_json()
    customer_id = data.get('customer_id')
    product_id = data.get('product_id')
    return shoppingCart.remove_product_from_cart(customer_id, product_id)

@token_required
def get_cart_items(customer_id):
    return shoppingCart.get_cart_items(customer_id)