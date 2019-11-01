SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
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

def melon_prices(melon_type, melon_tallies):
    """ calculates the earnings per melon type """

    melon_prices = { 'Musk': 1.15, 'Hybrid': 1.30, 'Watermelon': 1.75, 'Winter': 4.00 }

    melon_earnings = (melon_tallies[melon_type], melon_prices[melon_type])

    return melon_earnings


def orders_by_sales():
    sales_stats = open("orders-with-sales.txt")



print(DIVIDER)
print('* * * THE MELON REPORT * * *')
print(DIVIDER)

melon_tallies = melons_by_type()
total_revenue = 0
total_melons = 0

for melon in melon_tallies:
    melon_info = melon_prices(melon, melon_tallies)
    earnings = melon_info[0] * melon_info[1]
    total_revenue += earnings
    total_melons += melon_tallies[melon]
    print(f'We sold {melon_info[0]} {melon} at ${melon_info[1]} for a total of ${earnings:.2f}.')

print(f'We sold a total of {total_melons} melons for a total revenue of ${total_revenue:.2f}.')

"""
print(DIVIDER)
f = open("orders-with-sales.txt")
sales = [0, 0]
for line in f:
    d = line.split("|")
    if d[1] == "0":
        sales[0] += float(d[3])
    else:
        sales[1] += float(d[3])
print("Salespeople generated ${:.2f} in revenue.".format(sales[1]))
print("Internet sales generated ${:.2f} in revenue.".format(sales[0]))
if sales[1] > sales[0]:
    print("Guess there's some value to those salespeople after all.")
else:
    print("Time to fire the sales team! Online sales rule all!")
print(DIVIDER)
"""
