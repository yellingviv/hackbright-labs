"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries

from random import choice
import customers

def pick_winner(customer_list):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customer_list)

    print("Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        ))


def run_raffle():
    """Run the weekly raffle."""

    customer_list = customers.get_customers_from_file("customers.txt")
    pick_winner(customer_list)

run_raffle()
