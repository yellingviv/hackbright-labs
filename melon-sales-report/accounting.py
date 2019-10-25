SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DIVIDER = "* " * 20

def melons_by_type(melon_type_order):
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

def melon_prices(melon_type):
    """ calculates the earnings per melon type """

    melon_prices = { 'Musk': 1.15, 'Hybrid': 1.30, 'Watermelon': 1.75, 'Winter': 4.00 }

    melon_earnings = melon_tallies[melon_type] * melon_prices[melon_type]

return melon_earnings



print(DIVIDER)
print('* * * THE MELON REPORT * * *')
print(DIVIDER)


melon_prices = { 'Musk': 1.15, 'Hybrid': 1.30, 'Watermelon': 1.75, 'Winter': 4.00 }
total_revenue = 0
for melon_type in melon_tallies:
    price = melon_prices[melon_type]
    revenue = price * melon_tallies[melon_type]
    total_revenue += revenue
    # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
    print("We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue))
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
