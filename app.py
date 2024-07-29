from flask import Flask, request
#Flask - gives us all the tools we need to run a flask app by creating an instance of this class
from flask_sqlalchemy import SQLAlchemy
#SQLAlchemy = ORM to connect and relate python classes to SQL tables
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
#DeclarativeBase - gives us the base model functionality to create the Classes as Model Classes for our DB Tables
#Mapped- Maps a Class attribute to a table column or relationship
#mapped_column - sets out Column and allows us to add any constraints we need (unique, nullable, primary_key)
from flask_marshmallow import Marshmallow
#Marshmallow allows us to create a schema to validate, serialize and de-serialize JSON data
from datetime import date, timedelta
#date - use to create date type objects
from typing import List
#List - is used to create a relationship that will return a list of objects
from marshmallow import fields, ValidationError
#Fields - lets us set a schema field which includes and constraints
from sqlalchemy import select, delete, func
#selects - acts as our SELECT FROM query
#delete - acts as our DELETE query

from flask import Flask
from database import db
from models.schemas import ma

from models.customer import Customer
from models.order import Orders
from models.product import Products
from models.orderProduct import order_products
from models.role import Role

from routes.customerBP import customer_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint
from routes.shoppingCartBP import shopping_cart_blueprint
from limiter import limiter

from sample_data import add_sample_data

from flask_swagger_ui import get_swaggerui_blueprint

#SWAGGER
SWAGGER_URL = '/api/docs' #URL endpoint for Swagger UI Documentation
API_URL = '/static/swagger.yaml'

swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'Ecommerce API'})

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    
    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(shopping_cart_blueprint, url_prefix='/cart')

    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

def rate_limit_config():
    limiter.limit("800 per day")(customer_blueprint)
    limiter.limit("1000 per day")(product_blueprint)
    limiter.limit("1000 per day")(order_blueprint)
    limiter.limit("1000 per day")(shopping_cart_blueprint)
    limiter.limit("2000 per day")(swagger_blueprint)


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)

    with app.app_context():
        db.drop_all()
        db.create_all()
        add_sample_data()

    app.run()