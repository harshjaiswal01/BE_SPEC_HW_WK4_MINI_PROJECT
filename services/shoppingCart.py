from database import db #need db be to serve incoming data to db
from models.product import Products #need this to create Product Objects
from sqlalchemy import select, delete, func
from marshmallow import fields, ValidationError
from flask import Flask, jsonify, request

from models.customer import Customer
from models.product import Products
from models.shoppingCart import ShoppingCart
from models.schemas.shoppingcart import shopping_cart_schema, shopping_carts_schema


def add_product_to_cart(customer_id, product_id, quantity=1):
    try:
        # Check if the product exists
        query = select(Products).filter(Products.id == product_id)
        product = db.session.execute(query).scalars().first()
        if not product:
            raise ValidationError("Product not found")

        # Check if the customer exists
        query = select(Customer).filter(Customer.id == customer_id)
        customer = db.session.execute(query).scalars().first()
        if not customer:
            raise ValidationError("Customer not found")

        # Check if the product is already in the cart
        query = select(ShoppingCart).filter(
            ShoppingCart.customer_id == customer_id,
            ShoppingCart.product_id == product_id
        )
        cart_item = db.session.execute(query).scalars().first()

        if cart_item:
            cart_item.quantity += quantity  # Update the quantity if product is already in the cart
        else:
            # Add new product to cart
            cart_item = ShoppingCart(customer_id=customer_id, product_id=product_id, quantity=quantity)
            db.session.add(cart_item)

        db.session.commit()
        return jsonify({"message": "Product added to cart successfully"}), 201

    except ValidationError as e:
        return jsonify({"message": str(e)}), 400

    except Exception as e:
        return jsonify({"message": "An error occurred while adding the product to the cart", "error": str(e)}), 500

def remove_product_from_cart(customer_id, product_id):
    try:
        # Check if the cart item exists
        query = select(ShoppingCart).filter(
            ShoppingCart.customer_id == customer_id,
            ShoppingCart.product_id == product_id
        )
        cart_item = db.session.execute(query).scalars().first()
        if not cart_item:
            raise ValidationError("Product not found in cart")

        query = delete(ShoppingCart).where(
            ShoppingCart.customer_id == customer_id,
            ShoppingCart.product_id == product_id
        )
        db.session.execute(query)
        db.session.commit()
        return jsonify({"message": "Product removed from cart"}), 200

    except ValidationError as e:
        return jsonify({"message": str(e)}), 400

    except Exception as e:
        return jsonify({"message": "An error occurred while removing the product from the cart", "error": str(e)}), 500

def get_cart_items(customer_id):
    try:
        # Fetch all cart items for the customer
        query = select(ShoppingCart).filter(ShoppingCart.customer_id == customer_id)
        cart_items = db.session.execute(query).scalars().all()
        return shopping_carts_schema.jsonify(cart_items), 200

    except Exception as e:
        return jsonify({"message": "An error occurred while fetching the cart items", "error": str(e)}), 500
