"""A prefix-notation calculator.

Uses functions in arithmetic.py
Limited to a pre-defined number of integer inputs.
"""

from arithmetic import *


print('Welcome to the prefix calculator.')
print('Please enter a mathematical function and integers to be evaluated.')
print(f'Available functions:\n+ : sum two integers\n- : subtract two integers\n* : multiply two integers\n/ : divide the first integer by the second integer\nsq : square two integers\ncube : cube two integers\npow : raise one integer to the power of the second integer\nmod : return the remainder of the first integer divided by the second\nq : quit')

while True:

    to_math = input('Input an operation and two integers > ')
    equation = to_math.split(" ")

    if equation[0] == 'q':
        exit()
    elif len(equation) == 3:
        op = equation[0]
        num1 = int(equation[1])
        num2 = int(equation[2])
        if equation[0] == '+':
            print(add(num1, num2))
    else:
        print('Please review the instructions and enter correct input.')