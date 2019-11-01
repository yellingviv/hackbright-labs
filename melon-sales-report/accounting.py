DIVIDER = "* " * 20


def melons_by_type():
    """ cycles through the melon orders by type file to accumulate total melons ordered """

    melon_orders = open('orders-by-type.txt')
    melon_tallies = { 'Musk': 0, 'Hybrid': 0, 'Watermelon': 0, 'Winter': 0 }

    for line in melon_orders:
        order = line.split('|')
        melon_type = order[1]
        melon_count = int(order[2])
        melon_tallies[melon_type] += melon_count

    melon_orders.close()

    return melon_tallies

def melon_prices(melon_tallies):
    """ calculates the earnings per melon type """

    melon_prices = { 'Musk': 1.15, 'Hybrid': 1.30, 'Watermelon': 1.75, 'Winter': 4.00 }
    melon_earnings = {}

    for melon in melon_prices:
        melon_income = melon_tallies[melon] * melon_prices[melon]
        melon_earnings[melon] = { 'price': melon_prices[melon], 'income': melon_income }

    return melon_earnings


def orders_by_sales():
    sales_stats = open("orders-with-sales.txt")
    sales = { 'Salespeople': 0,
    'Internet': 0 }

    for sale in sales_stats:
        sale = sale.split('|')
        if sale[1] == '0':
            sales['Internet'] += float(sale[3])
        else:
            sales['Salespeople'] += float(sale[3])
    sales_stats.close()

    return sales

def people_vs_internet(sales):
    if sales['Salespeople'] > sales['Internet']:
        return True
    else:
        return False


melon_tallies = melons_by_type()
melon_earnings = melon_prices(melon_tallies)
total_revenue = 0
total_melons = 0
sales = orders_by_sales()

print(DIVIDER)
print('* * * * * * THE MELON REPORT * * * * * *')
print(DIVIDER)
print('\n')

for melon in melon_tallies:
    total_revenue += melon_earnings[melon]['income']
    total_melons += melon_tallies[melon]
    print(f"We sold {melon_tallies[melon]} {melon} at ${melon_earnings[melon]['price']} for a total of ${melon_earnings[melon]['income']:.2f}.")

print('\n')
print(f'We sold a total of {total_melons} melons for a total revenue of ${total_revenue:.2f}.')

print('\n')
print(DIVIDER)
print('\n')

print(f"Salespeople generated ${sales['Salespeople']:.2f} in revenue.")
print(f"Internet sales generated ${sales['Internet']:.2f} in revenue.")
print('\n')

if people_vs_internet:
    print("Guess there's some value to those salespeople after all.")
else:
    print("Time to fire the sales team! Online sales rule all!")

print('\n')
print(DIVIDER)
