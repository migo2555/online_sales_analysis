# product_manager.py
from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Product '{product_name}' removed successfully.")
                return
        print(f"Product '{product_name}' not found.")

    def display_all_products(self):
        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):
        return sum(product.price * product.quantity for product in self.products)

