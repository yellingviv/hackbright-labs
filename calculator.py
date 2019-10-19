"""A prefix-notation calculator.

Uses functions in arithmetic.py
Limited to a pre-defined number of integer inputs.
"""

from arithmetic import *


print('* * * Welcome to the prefix calculator * * *')
print('This calculator takes integer input and returns floats.')
print('Please enter a mathematical function and integers to be evaluated.')
print(f'Available functions:\n+ : sum two integers\n- : subtract two integers\n* : multiply two integers\n/ : divide the first integer by the second integer\nsq : square two integers\ncube : cube two integers\npow : raise one integer to the power of the second integer\nmod : return the remainder of the first integer divided by the second\nq : quit')

while True:

    to_math = input('Input an operation and two integers > ')
    equation = to_math.split(" ")

    def fail():
        print('Please review the instructions and enter correct input.')

    if equation[0] == 'q':
        exit()
    elif len(equation) == 2:
        op = equation[0]
        num1 = int(equation[1])
        if op == 'sq':
            print(square(num1))
        elif op == 'cube':
            print(cube(num1))
        else:
            fail()
    elif len(equation) == 3:
        op = equation[0]
        num1 = int(equation[1])
        num2 = int(equation[2])
        if op == '+':
            print(add(num1, num2))
        elif op == '-':
            print(subtract(num1, num2))
        elif op == '*':
            print(multiply(num1, num2))
        elif op == '/':
            print(divide(num1, num2))
        elif op == 'pow':
            print(power(num1, num2))
        elif op == 'mod':
            print(mod(num1, num2))
    else:
        fail()