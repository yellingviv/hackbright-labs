"""A prefix-notation calculator.

Uses functions in arithmetic.py
Limited to a pre-defined number of float inputs."""

from arithmetic import *
# important the arithmetic.py module


print('* * * Welcome to the prefix calculator * * *')
print('This calculator takes float input and returns floats.')
print('Please enter a mathematical function and numbers to be evaluated.')
print(f'Available functions:\n+ : sum two numbers\n- : subtract two numbers\n* : multiply two numbers\n/ : divide the first number by the second\nsq : square two numbers\ncube : cube two numbers\npow : raise one number to the power of the second number\nmod : return the remainder of the first number divided by the second\nq : quit')
# inform the user of what is available

while True:

    to_math = input('Input an operation and two numbers > ')
    # request the mathematical activity and numbers to operate on from the user
    equation = to_math.split(" ")
    # tokenize the user input! IE turn the math activity and the numbers into a list

    def fail():
        # a function to let a user know that they didn't follow directions
        print('Please review the instructions and enter correct input.')

    if equation[0] == 'q':
        # user wants to quit
        exit()
    elif len(equation) == 2:
        # only an operand and one digit is present
        op = equation[0]
        num1 = float(equation[1])
        # identify the operation and the number
        if op == 'sq':
            print(square(num1))
        elif op == 'cube':
            print(cube(num1))
        else:
            # the math action isn't possible with only one number
            fail()
    elif len(equation) == 3:
        # an operand and two digits are present
        op = equation[0]
        num1 = float(equation[1])
        num2 = float(equation[2])
        # identify the operand and the two numbers
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
        # something went wrong, idk, bail out!
        fail()