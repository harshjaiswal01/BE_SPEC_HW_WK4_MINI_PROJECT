from datetime import date, timedelta
from werkzeug.security import generate_password_hash
from database import db
from models.customer import Customer
from models.order import Orders
from models.product import Products
from models.role import Role
from models.shoppingCart import ShoppingCart

def add_sample_data():
    # Create sample roles
    admin_role = Role(role_name="Admin")
    user_role = Role(role_name="User")

    db.session.add(admin_role)
    db.session.add(user_role)
    db.session.commit()

    # Create sample customers
    customer1 = Customer(
        customer_name="John Doe",
        email="john.doe@example.com",
        phone="1234567890",
        username="johndoe",
        password="password123",
        role_id=user_role.id
    )

    customer2 = Customer(
        customer_name="Jane Smith",
        email="jane.smith@example.com",
        phone="0987654321",
        username="janesmith",
        password="password456",
        role_id=admin_role.id
    )

    db.session.add(customer1)
    db.session.add(customer2)
    db.session.commit()

    # Create sample products
    products = [
        Products(product_name="Toothpaste", price=3.49),
        Products(product_name="Shampoo", price=5.99),
        Products(product_name="Soap", price=1.99),
        Products(product_name="Laundry Detergent", price=8.49),
        Products(product_name="Dish Soap", price=2.99),
        Products(product_name="Paper Towels", price=4.99),
        Products(product_name="Toilet Paper", price=6.99),
        Products(product_name="Trash Bags", price=7.99),
        Products(product_name="Aluminum Foil", price=2.49),
        Products(product_name="Plastic Wrap", price=2.99),
        Products(product_name="Glass Cleaner", price=3.99),
        Products(product_name="All-Purpose Cleaner", price=4.49),
        Products(product_name="Sponges", price=3.29),
        Products(product_name="Bleach", price=2.99),
        Products(product_name="Air Freshener", price=3.59),
        Products(product_name="Batteries", price=5.99),
        Products(product_name="Light Bulbs", price=6.49),
        Products(product_name="Fabric Softener", price=4.99),
        Products(product_name="Disinfecting Wipes", price=4.79),
        Products(product_name="Hand Sanitizer", price=3.99)
    ]

    db.session.add_all(products)
    db.session.commit()

    # Create sample orders
    order1 = Orders(
        order_date=date.today(),
        customer_id=customer1.id,
        expected_delivery_date=date.today() + timedelta(days=7)
    )

    order2 = Orders(
        order_date=date.today(),
        customer_id=customer2.id,
        expected_delivery_date=date.today() + timedelta(days=7)
    )

    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()

    # Associate products with orders
    order1.products.append(products[0])
    order1.products.append(products[1])
    order2.products.append(products[2])

    db.session.commit()

    # Add sample shopping cart data
    cart_item1 = ShoppingCart(
        customer_id=customer1.id,
        product_id=products[2].id,
        quantity=2
    )

    cart_item2 = ShoppingCart(
        customer_id=customer1.id,
        product_id=products[3].id,
        quantity=1
    )

    cart_item3 = ShoppingCart(
        customer_id=customer2.id,
        product_id=products[4].id,
        quantity=3
    )

    cart_item4 = ShoppingCart(
        customer_id=customer2.id,
        product_id=products[5].id,
        quantity=1
    )

    db.session.add(cart_item1)
    db.session.add(cart_item2)
    db.session.add(cart_item3)
    db.session.add(cart_item4)
    db.session.commit()

    print("Sample data added successfully.")
