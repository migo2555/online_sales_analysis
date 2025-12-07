# Online Sales Analysis

A Python project for managing and analyzing online sales data.  
Includes a `Product` class with attributes for name, price, and quantity, along with classes for inventory management (`ProductManager`) and a shopping cart (`Cart`).

## Features

- **Product Management**: Add, display, remove products; calculate total inventory value.
- **Shopping Cart**: Add products to cart, display cart contents, calculate total cart value.
- **Data Handling**: Load products from `product_info.csv`; optional `config.json` for configuration.

## Project Structure

online_sales_analysis/
├── product.py            # Product class
├── product_manager.py    # ProductManager class
├── cart.py               # Cart class
├── main.py               # Main script
├── product_info.csv      # Sample product data
├── config.json           # Optional config file
└── .gitignore            # Git ignore rules

## Example Usage

```python
from product import Product
from product_manager import ProductManager
from cart import Cart

# Create products and manager
manager = ProductManager()
manager.add_product(Product("Laptop", 1200.99, 5))
manager.add_product(Product("Mouse", 25.50, 15))

# Display available products
manager.display_all_products()

# Create a cart and add products
cart = Cart()
cart.add_to_cart(manager.products[0], 1)
cart.display_cart()
print("Total Cart Value:", cart.calculate_total())

```
This demonstrates adding products to the inventory, displaying them, and simulating a shopping cart.
