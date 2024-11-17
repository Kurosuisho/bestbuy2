class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = float(quantity)
        self.active = True

    def get_quantity(self):
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the product's quantity. Deactivates the product if quantity is 0."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        self.quantity = float(quantity)
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        Buys a specified quantity of the product.
        Returns the total price for the purchase.
        Raises an exception if the quantity is invalid or insufficient.
        """
        if not self.is_active():
            raise Exception("Product is inactive.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price
    


class NonStockedProducts(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        raise Exception("Cannot set quantity for non-stocked products.")

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        return self.price * quantity

    def show(self):
        return f"{super().show()} (Non-Stocked Product)"


class LimitedProducts(Product):
    def __init__(self, name, price, quantity, max_per_order):
        super().__init__(name, price, quantity)
        if max_per_order <= 0:
            raise ValueError("max_per_order must be greater than zero.")
        self.max_per_order = max_per_order

    def buy(self, quantity):
        if quantity > self.max_per_order:
            raise Exception(f"Cannot buy more than {self.max_per_order} of this product per order.")
        return super().buy(quantity)

    def show(self):
        return f"{super().show()} (Limited to {self.max_per_order} per order)"


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
    
if __name__ == "__main__":
    main()
