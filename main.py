
import products
import store

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(best_buy):
    """Displays a menu for the user and performs actions based on the selection."""
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
            print("\nProducts available in store:")
            print("----------")
            for product in products:
                product_name = product.name
                product_price = product.price
                product_quantity = product.get_quantity()
                print(f"- {product_name}, Price: ${product_price}, Quantity: {product_quantity}")
            print("----------")

        elif choice == "2":
            # Show total quantity of products in the store
            total_quantity = best_buy.get_total_quantity()
            print(f"\nTotal quantity of {total_quantity} products in store1")

        elif choice == "3":
            # Make an order
            order = []
            products = best_buy.get_all_products()

            # Display available products with numbered list
            print("\n------")
            for idx, product in enumerate(products, start=1):
                product_name = product.name
                product_price = product.price
                product_quantity = product.get_quantity()
                print(f"{idx}. {product_name}, Price: ${product_price}, Quantity: {product_quantity}")
            print("------")
            print("When you want to finish order, enter empty text.")

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
            total_price = best_buy.order(order)
            print("\nTotal price for your order:")
            print(f"${total_price:.2f}")

        elif choice == "4":
            # Quit the program
            print("Thank you for visiting! Goodbye.")
            break

        else:
            # Handle invalid choice
            print("Invalid choice. Please enter a number between 1 and 4.")


start(best_buy)