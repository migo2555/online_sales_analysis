# main.py

from product_manager import ProductManager
from product import Product
from cart import Cart
import random

def main():
    manager = ProductManager()

    # Dodavanje proizvoda
    manager.add_product(Product("Laptop", 1200.99, 5))
    manager.add_product(Product("Mouse", 25.50, 15))
    manager.add_product(Product("Keyboard", 45.00, 10))
    manager.add_product(Product("Monitor", 250.75, 7))
    manager.add_product(Product("Headphones", 89.99, 12))   
    manager.add_product(Product("Webcam", 59.90, 8))        

    print(" Available Products:")
    manager.display_all_products()

    # Ukupna vrednost inventara
    total_value = manager.total_inventory_value()
    print(f"\n Total Inventory Value: ${total_value:.2f}")

    # Kreiranje korpe
    cart = Cart()

    products = manager.products
    for _ in range(3):
        product = random.choice(products)
        max_quantity = min(product.quantity, 3)
        if max_quantity > 0:
            quantity = random.randint(1, max_quantity)
            cart.add_to_cart(product, quantity)

    print("\n Cart Contents:")
    cart.display_cart()

    cart_total = cart.calculate_total()
    print(f"\n Total Cart Value: ${cart_total:.2f}")

if __name__ == "__main__":
    main()
