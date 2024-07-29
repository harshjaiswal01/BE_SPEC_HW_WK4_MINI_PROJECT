from database import db #need db be to serve incoming data to db
from models.order import Orders #need this to create Product Objects
from sqlalchemy import select, delete, func
from marshmallow import fields, ValidationError
from flask import Flask, jsonify, request
from models.schemas.orderSchema import order_schema,orders_schema
from models.product import Products
from models.schemas.productSchema import product_schema, products_schema, products_schema2
from models.customer import Customer
from datetime import date, timedelta

def add_order(order_data):


    try:
        order_data = order_schema.load(order_data)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    
    future_date = date.today() + timedelta(days = 3)
    
    new_order = Orders(order_date = date.today(), customer_id = order_data["customer_id"], expected_delivery_date = future_date)

    querycus = select(Customer).filter(Customer.id == new_order.customer_id)
    resultcus = db.session.execute(querycus).scalars().first()

    if resultcus is None:
        return None, jsonify({"Error":"Customer not found"})

    for item_id in order_data['items']:
        query = select(Products).filter(Products.id == item_id)
        item = db.session.execute(query).scalar()
        # print(items)

        if item is None:
            return None, jsonify({"Error":"Product not found!!!"})
        new_order.products.append(item)

    db.session.add(new_order)
    db.session.commit()
    new_order_id = new_order.id
    # print ("ORder ID is ", new_order.id)
    # return jsonify({f"Message":"New Order Placed", "Order ID":new_order_id}),201
    return new_order, None

def order_items(id):
    query = select(Orders).filter(Orders.id == id)

    order = db.session.execute(query).scalar()
    if order is None:
        return None, {"Error": "Order does not exist"}
    return order.products, None

def get_order_paginated(page, per_page):
    query = select(Orders)
    print("Query is ", query)
    order = db.paginate(query, page=page, per_page=per_page)
    if order is None:
        return None, {"Error": "Order does not exist"}
    # print(order.products)
    return order, None
    
def order_tracking(id):
    query = select(Orders).filter(Orders.id == id)
    order = db.session.execute(query).scalar()
    try:
        # print ("Order Details" , order.id, order.order_date, order.expected_delivery_date)
        # # return order_schema.jsonify(order)
        return jsonify({"Order ID":order.id,"Customer ID":order.customer_id ,"Order Date":order.order_date, "Expected Delivery Date":order.expected_delivery_date}), None
    except AttributeError as e:
        return None, jsonify({"Error":"Order Doesnot Exist"})


from models.shoppingCart import ShoppingCart

def add_order_from_cart(customer_id):
    try:
        # Check if the customer exists
        querycus = select(Customer).filter(Customer.id == customer_id)
        customer = db.session.execute(querycus).scalars().first()

        if customer is None:
            return None, jsonify({"Error": "Customer not found"})

        # Fetch all items in the shopping cart for the customer
        query_cart = select(ShoppingCart).filter(ShoppingCart.customer_id == customer_id)
        cart_items = db.session.execute(query_cart).scalars().all()

        if not cart_items:
            return None, jsonify({"Error": "Shopping cart is empty"})

        # Create a new order
        future_date = date.today() + timedelta(days=3)
        new_order = Orders(order_date=date.today(), customer_id=customer_id, expected_delivery_date=future_date)

        # Add products from the cart to the order
        for cart_item in cart_items:
            product_query = select(Products).filter(Products.id == cart_item.product_id)
            product = db.session.execute(product_query).scalars().first()
            if product:
                new_order.products.append(product)
        
        # Clear the shopping cart
        delete_cart_query = delete(ShoppingCart).filter(ShoppingCart.customer_id == customer_id)
        db.session.execute(delete_cart_query)

        db.session.add(new_order)
        db.session.commit()

        return new_order, None

    except ValidationError as e:
        return jsonify(e.messages), 400

    except Exception as e:
        return jsonify({"message": "An error occurred while creating the order", "error": str(e)}), 500
