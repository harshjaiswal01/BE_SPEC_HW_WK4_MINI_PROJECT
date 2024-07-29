
# Ecommerce API

This project provides an API to manage ecommerce interactions, including customer management, product management, order processing, and shopping cart functionality.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Customers](#customers)
  - [Orders](#orders)
  - [Products](#products)
  - [Shopping Cart](#shopping-cart)
- [Security](#security)
- [License](#license)

## Features

- **Customer Management**: Add, update, delete, and retrieve customer information.
- **Product Management**: Add, update, delete, and retrieve product information.
- **Order Processing**: Create orders from products and shopping cart items.
- **Shopping Cart**: Add and remove products from the shopping cart and create orders from the cart.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ecommerce-api.git
   cd ecommerce-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the application:
   ```bash
   flask run
   ```

## API Endpoints

### Customers

- **Login**
  ```http
  POST /customers/login
  ```
  - Request Body: `username`, `password`
  - Response: `auth_token`, `message`, `status`

- **Get All Customers**
  ```http
  GET /customers
  ```
  - Headers: `Authorization: Bearer <token>`
  - Response: List of customers

- **Add Customer**
  ```http
  POST /customers
  ```
  - Headers: `Authorization: Bearer <token>`
  - Request Body: `customer_name`, `email`, `phone`, `username`, `password`, `role_id`
  - Response: Added customer

- **Get Customer by ID**
  ```http
  GET /customers/{id}
  ```
  - Headers: `Authorization: Bearer <token>`
  - Response: Customer information

- **Update Customer**
  ```http
  PUT /customers/{id}
  ```
  - Headers: `Authorization: Bearer <token>`
  - Request Body: Updated customer data
  - Response: Updated customer

- **Delete Customer**
  ```http
  DELETE /customers/{id}
  ```
  - Headers: `Authorization: Bearer <token>`
  - Response: Success message

### Orders

- **Add Order**
  ```http
  POST /orders
  ```
  - Headers: `Authorization: Bearer <token>`
  - Request Body: `customer_id`, `items`
  - Response: Added order

- **Add Order from Cart**
  ```http
  POST /orders/from_cart
  ```
  - Headers: `Authorization: Bearer <token>`
  - Request Body: `customer_id`
  - Response: Added order from cart

- **Get Order Items**
  ```http
  GET /orders/{id}
  ```
  - Headers: `Authorization: Bearer <token>`
  - Response: List of order items

- **Track Order**
  ```http
  GET /orders/track/{id}
  ```
  - Headers: `Authorization: Bearer <token>`
  - Response: Order tracking information

- **Paginate Orders**
  ```http
  GET /orders/p
  ```
  - Headers: `Authorization: Bearer <token>`
  - Query Params: `page`, `per_page`
  - Response: Paginated orders

### Products

- **Get All Products**
  ```http
  GET /products
  ```
  - Headers: `Authorization: Bearer <token>`
  - Response: List of products

- **Add Product**
  ```http
  POST /products
  ```
  - Headers: `Authorization: Bearer <token>`
  - Request Body: `product_name`, `price`
  - Response: Added product

- **Get Product by ID**
  ```http
  GET /products/{id}
  ```
  - Headers: `Authorization: Bearer <token>`
  - Response: Product information

- **Update Product**
  ```http
  PUT /products/{id}
  ```
  - Headers: `Authorization: Bearer <token>`
  - Request Body: Updated product data
  - Response: Updated product

- **Delete Product**
  ```http
  DELETE /products/{id}
  ```
  - Headers: `Authorization: Bearer <token>`
  - Response: Success message

- **Paginate Products**
  ```http
  GET /products/p
  ```
  - Headers: `Authorization: Bearer <token>`
  - Query Params: `page`, `per_page`
  - Response: Paginated products

### Shopping Cart

- **Add Product to Cart**
  ```http
  POST /cart/add
  ```
  - Headers: `Authorization: Bearer <token>`
  - Request Body: `customer_id`, `product_id`, `quantity`
  - Response: Added product to cart

- **Remove Product from Cart**
  ```http
  POST /cart/remove
  ```
  - Headers: `Authorization: Bearer <token>`
  - Request Body: `customer_id`, `product_id`
  - Response: Removed product from cart

- **Get Cart Items**
  ```http
  GET /cart/{customer_id}
  ```
  - Headers: `Authorization: Bearer <token>`
  - Response: List of cart items

## Security

This API uses JWT (JSON Web Token) for authentication. Include the token in the `Authorization` header with the `Bearer ` prefix for authenticated endpoints.

## License

This project is licensed under the MIT License.
