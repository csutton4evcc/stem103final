# Import Coffee Shop Functions
from coffee_shop import *

# Getting User Information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Validating and getting a 10-digit phone number from the user
check_phone()

# Setting up the Coffee Shop
menu = initialize_store(first_name, last_name)

# Initializing Cart
total_cost, cart = 0, []

# Taking Coffee Orders
total_cost = take_order(menu, total_cost, cart)

# Calculating Tax (10%)
tax = total_cost * 0.10
total_cost_with_tax = total_cost + tax

# Displaying the Order Summary with Tax
print_total(cart, tax, total_cost, total_cost_with_tax)

# Thank You Message
thank_you()

