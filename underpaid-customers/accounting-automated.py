""" M E L O N - A C C O U N T I N G
iterate through a file of customer purchases
identify how many melons were purchased and how much was paid
flag if a customer over paid or under paid and report accordingly """

accounting_file = open('customer-orders.txt')

melon_price = 1.00
underpaid_count = 0
overpaid_count = 0
total_orders = 0

print('* * * DAILY MELON ORDER REVIEW * * *')
print('')
for line in accounting_file:
    line = line.rstrip()
    order = line.split('|')
    customer_num = order[0]
    customer_name = order[1]
    melon_order = int(order[2])
    paid = float(order[3])
    correct_payment = melon_order * melon_price

    print(f'Customer number {customer_num}, {customer_name}, ordered {melon_order} melons, and paid ${paid}.')

    total_orders += 1

    if paid != correct_payment:
        print(f'     * * * This order payment is INCORRECT. {customer_name} should have paid ${correct_payment}.')
        if paid < correct_payment:
            print(f'     * * * This payment is UNDERPAID. {customer_name} owes ${correct_payment - paid}. Please contact {customer_name} for additional payment.')
            underpaid_count += 1
        elif paid > correct_payment:
            print(f'     * * * This payment is OVERPAID. {customer_name} overpaid by ${correct_payment - paid}. Please issue {customer_name} a refund.')
            underpaid_count += 1

print('')
print('* * * TOTAL DAILY SUMMARY * * *')
print('')
print(f'Today Ubermelon processed a total of {total_orders}.')
print(f'There were {underpaid_count} underpaid orders in need of additional payment.')
print(f'There were {overpaid_count} overpaid orders in need of reimbursement.')
