"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
print('Welcome to the prefix calculator.')
print('Please enter a mathematical function and integers to be evaluated.')
print(f'Available functions:\n+ : sum two integers\n- : subtract two integers\n* : multiply two integers\n/ : divide the first integer by the second integer\nsq : square two integers\ncube : cube two integers\npow : raise one integer to the power of the second integer\nmod : return the remainder of the first integer divided by the second')

to_math = input('Input an operation and two integers > ')

print(to_math)