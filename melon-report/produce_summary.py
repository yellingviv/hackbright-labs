""" This prints out the reports of the daily melon deliveries for Ubermelon"""

def delivery_info(delivery_file):
    daily_count = 0
    daily_amount = 0
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = int(words[1])
        amount = float(words[2])

        daily_count = daily_count + count
        daily_amount = daily_amount + amount

        print("     Delivered {} {}s for total of ${}".format(count, melon, amount))

    daily = [daily_count, daily_amount]
    return daily


print("Day 1")
the_file = open("um-deliveries-20140519.txt")
daily_results = delivery_info(the_file)

print('')
print(f'Day 1\'s Total: {daily_results[0]} melons for a total of ${daily_results[1]}.')
the_file.close()

"""
print('')
print('')

print("Day 2")
the_file = open("um-deliveries-20140520.txt")
daily_count = 0
daily_amount = 0
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = int(words[1])
    amount = float(words[2])

    daily_count = daily_count + count
    daily_amount = daily_amount + amount

    print("     Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()

print('')
print(f'Day 2\'s Total: {daily_count} melons for a total of ${daily_amount}.')
the_file.close()

print('')
print('')

print("Day 3")
the_file = open("um-deliveries-20140521.txt")
daily_count = 0
daily_amount = 0
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = int(words[1])
    amount = float(words[2])

    daily_count = daily_count + count
    daily_amount = daily_amount + amount

    print("     Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()

print('')
print(f'Day 3\'s Total: {daily_count} melons for a total of ${daily_amount}.')
the_file.close()"""