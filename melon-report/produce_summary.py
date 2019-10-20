""" This prints out the reports of the daily melon deliveries for Ubermelon"""

def delivery_info(delivery_file):
    # iterate through the delivery file to establish the total sales for the day

    daily_count = 0
    daily_amount = 0
    # start with the count and price of melons sold at zero

    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = int(words[1])
        amount = float(words[2])

        daily_count = daily_count + count
        daily_amount = daily_amount + amount
        # add the count of melons and price of melons for this line to the daily total

        print("     Delivered {} {}s for total of ${}".format(count, melon, amount))
        # print only the quantity of melons and total cost for that specific melon varietal

    daily = [daily_count, daily_amount]
    return daily
    # return back the daily total quantity of melons sold for total price

print("Day 1")
the_file = open("um-deliveries-20140519.txt")
# select the file for that day - should be possible to do this more cleanly

daily_results = delivery_info(the_file)
# pass the daily delivery info file to the evaluation function

print('')
print(f'Day 1\'s Total: {daily_results[0]} melons for a total of ${daily_results[1]}.')
# print the total sold and earned for the day
the_file.close()
# close the file to move to the next day's file

print('')
print('')

print("Day 2")
the_file = open("um-deliveries-20140520.txt")
daily_results = delivery_info(the_file)

print('')
print(f'Day 2\'s Total: {daily_results[0]} melons for a total of ${daily_results[1]}.')
the_file.close()

print('')
print('')

print("Day 3")
the_file = open("um-deliveries-20140521.txt")
daily_results = delivery_info(the_file)

print('')
print(f'Day 3\'s Total: {daily_results[0]} melons for a total of ${daily_results[1]}.')
the_file.close()

print('')
print('')