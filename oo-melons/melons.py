"""Classes for melon orders."""

from random import randint
from datetime import time 

class AbstractMelonOrder():

    def __init__(self, species, quantity, country_code='USA'):
        """instantiate a melon order"""

        self.species = species
        self.quantity = quantity
        self.shipped = False
        self.country_code = country_code

    def get_base_price(self):
        """Calculate base price, based on Splurge pricing"""

        base_price = randint(5, 9)
        return base_price

    def rush_hour_total(self):
        """Determine if order is placed between 8-11AM, M-F"""

        get_time = datetime.d

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        total = 0
        if self.species == 'Christmas':
            base_price *= 1.5
        if self.order_type == 'international' and self.quantity < 10:
            total += 3
        total = (1 + self.tax) * self.quantity * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    country_code = "USA"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17


class GovernmentMelonOrder(AbstractMelonOrder):
    """a melon order that is specific to government"""

    order_type = "government"
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True
