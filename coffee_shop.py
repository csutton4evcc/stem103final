# Coffee shop functions - must be included with main.py for the program to run

def check_phone():
    get_phone_number = True
    while get_phone_number:
        phone_number = input("Enter your 10-digit phone number: ")
        if phone_number.isdigit() is False or len(phone_number) != 10:
            print("Please enter a valid 10-digit phone number (i.e. 2068675309): ")
            continue
        else:
            get_phone_number = False


def initialize_store(first_name, last_name):
    coffee_shop_name = "STEM 103 Coffee Shop"
    print(f"Hello, {first_name} {last_name}! Welcome to {coffee_shop_name}.")
    print("=" * 50)
    menu = {
        1: {"name": "Black Coffee", "price": 3.25},
        2: {"name": "Latte", "price": 4.50},
        3: {"name": "Cappuccino", "price": 4.50},
        4: {"name": "Espresso", "price": 3.50},
        5: {"name": "Americano", "price": 3.50}
    }
    return menu


def take_order(menu, total_cost, cart):
    option = 0
    continue_menu = "True"
    while continue_menu:
        # Displaying the Menu
        print("\nMenu:")
        for key, item in menu.items():
            print(f"{key}. {item['name']}: ${item['price']:.2f}")

        # Getting the User's Choice
        option = int(input("Choose the coffee number you would like to order? (Enter '0' to proceed to checkout): "))

        # Adding the Selected Coffee to the Cart
        if option in menu:
            quantity = int(input("Enter the quantity: "))
            total = quantity * menu[option]["price"]
            total_cost += total
            cart.append((f"{quantity} x {menu[option]['name']} - ${total:.2f}", total))
        elif option == 0:
            continue_menu = False
        else:
            print("Invalid option. Please choose a valid coffee number.")
    return total_cost


def print_total(cart, tax, total_cost, total_cost_with_tax):
    print("*" * 50)
    print("Your Order Summary:\n")
    for item, price in cart:
        print(f"{item}")
    print("*" * 50)
    print(f"Subtotal: ${total_cost:.2f}")
    print(f"Tax (10%): ${tax:.2f}")
    print(f"Total Cost (Including Tax): ${total_cost_with_tax:.2f}")
    print("*" * 50)


def thank_you():
    print(f"Thank you for ordering! \n"
          f"You'll get a text when your coffee is ready.")
    print("Have a wonderful day!")
    print("*" * 50)



