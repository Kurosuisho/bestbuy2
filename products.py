
from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

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
        """Returns a f-string describing the product with possible promotions"""
        promo = self.promotion.name if self.promotion else "None"
        return f"{self.name}, Price: ${self.price}, Quantity: {int(self.quantity)}, Promotion: {promo}"

    def buy(self, quantity):
        """
        Buys a specified quantity of the product.
        Returns the total price for the purchase.
        Raises an exception if the quantity is invalid or insufficient.
        """
        if not self.active or quantity <= 0 or quantity > self.quantity:
            raise ValueError("Invalid purchase.")
        
        if self.promotion:
            price = self.promotion.apply_promotion(self.price, quantity)
        else:
            price = self.price * quantity

        self.quantity -= quantity
        self.active = self.quantity > 0
        return price
    
    def set_promotion(self, promotion):
        self.promotion = promotion


class Promotion(ABC):
    """Abstract base class for promotions."""
    @abstractmethod
    def apply_promotion(self, price, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        if not (0 <= percent <= 100):
            raise ValueError("Percent must be between 0 and 100.")
        self.name = name
        self.percent = percent

    def apply_promotion(self, price, quantity):
        return price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, price, quantity):
        discounted_items = quantity // 2
        return price * discounted_items * 0.5 + price * (quantity - discounted_items)


class ThirdOneFree(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, price, quantity):
        free_items = quantity // 3
        return price * (quantity - free_items)


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
        """Returns a f-string describing non-stocked products."""
        promo = self.promotion.name if self.promotion else "None"
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {promo}"


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
        """Returns a f-string describing limited products."""
        promo = self.promotion.name if self.promotion else "None"
        return f"{self.name}, Price: ${self.price}, Limited to {self.max_per_order} per order!, Promotion: {promo}"


#def main():
 #   bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
  #  mac = Product("MacBook Air M2", price=1450, quantity=100)
#
 #   print(bose.buy(50))
  #  print(mac.buy(100))
   # print(mac.is_active())
#
 #   bose.show()
  #  mac.show()
#
 #   bose.set_quantity(1000)
  #  bose.show()
   # 
#if __name__ == "__main__":
 #   main()
