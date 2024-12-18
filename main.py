import products
import store
from products import SecondHalfPrice, ThirdOneFree, PercentDiscount

def main():
    """Main function to initialize the store and start the application.

    This function sets up a list of predefined products, initializes the store with these products, 
    and starts the user interaction loop.

    Returns:
        None
    """
    # Create product list
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProducts("Windows License", price=125),
        products.LimitedProducts("Shipping", price=10, quantity=250, max_per_order=1),
    ]

    # Create promotions
    second_half_price = SecondHalfPrice("Second Half Price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% Off!", percent=30)

    # Assign promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    # Create the store
    best_buy = store.Store(product_list)

    # Start the store interaction loop
    start(best_buy)

def start(best_buy):
    """Displays a menu for the user and executes actions based on their selection.

    Args:
        best_buy (Store): The store object containing product inventory and operations.

    Returns:
        None
    """
    while True:
        # Display the menu options
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        # Get user choice
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            # List all products in the store
            products = best_buy.get_all_products()
            print("\n------")
            for index, product in enumerate(products, start=1):
                print(f"{index}. {product.show()}")
            print("------")

        elif choice == "2":
            # Show total quantity of products in the store
            total_quantity = best_buy.get_total_quantity()
            print(f"\nTotal quantity of {total_quantity} products in store!")

        elif choice == "3":
            # Make an order
            order = []
            products = best_buy.get_all_products()

            # Display available products with numbered list
            print("\n------")
            for index, product in enumerate(products, start=1):
                product_name = product.name
                product_price = product.price
                product_quantity = product.get_quantity()
                print(f"{index}. {product_name}, Price: ${product_price}, Quantity: {product_quantity}")
            print("------")
            print("When you want to the finish order, enter an empty text.")

            while True:
                # Prompt for product number
                product_choice = input("Which product # do you want? ")

                if product_choice.strip() == "":
                    # Exit order input if the user enters empty text
                    break

                try:
                    # Convert product number to index
                    product_index = int(product_choice) - 1

                    # Ensure product index is valid
                    if 0 <= product_index < len(products):
                        product_to_order = products[product_index]

                        # Prompt for quantity of chosen product
                        quantity = input(f"How many '{product_to_order.name}' would you like to order? ")

                        # Check if quantity is valid
                        if quantity.isdigit() and int(quantity) > 0:
                            order.append((product_to_order, int(quantity)))
                        else:
                            print("Invalid quantity. Please enter a positive number.")
                    else:
                        print("Invalid product number. Please choose a number from the list.")
                
                except ValueError:
                    print("Please enter a valid product number.")

            # Process the order and display the total price
            try:
                total_price = best_buy.order(order)
                print("\nTotal price for your order:")
                print(f"${total_price:.2f}")
            except Exception as e:
                print(f"Error processing order: {e}")

        elif choice == "4":
            # Quit the program
            print("Thank you for visiting! Goodbye.")
            break

        else:
            # Handle invalid choice
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
