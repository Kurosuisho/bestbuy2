
from products import Product

class Store:
    
    
    def __init__(self, products=[]):
        """Initializes with an empty list"""
        self.products = products


    def add_product(self, product):
        """Adds a product to the store"""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store"""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Returns the total quantity of all items in the store"""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        """Returns a list of all active products in the store"""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        """
        Processes an order based on a list of (Product, quantity) tuples
        Buys the products and returns the total price of the order
        Handles exceptions if there are issues with purchasing
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except ValueError as ve:
                # Handle specific issues such as negative quantity or insufficient stock
                print(f"Order error for '{product.name}': {ve}")
            except Exception as e:
                # Handle other general issues, like if the product is inactive
                print(f"Order error for '{product.name}': {e}")
        return total_price


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))
    
    
if __name__ == "__main__":
    main()