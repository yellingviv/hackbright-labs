"""This is a number-guessing game, leveraging module/function import and user input.
I repeatedly screwed up the commit and so on, so there's not commit history. Hashtag learning."""

from random import randint

print('Hello, and welcome to the number guessing game!')
player = input('What shall I call you, brave player? > ')
print(f'Welcome, noble {player}. Prepare yourself to...')
print('GUESS A NUMBER...')
print('Between... 1...')
print('And... 100!!')

true_num = randint(1, 100)

while True:
    guess_num = input('What is your guess? > ')
    guesses = 0
    if guess_num.isnumeric() is False:
        print('I see your cheeky attempts at outsmarting me, but that will not work!')
        print(f'Try again, sassy {player}, you!')
    elif int(guess_num) > 100:
        print('I see your cheeky attempts at outsmarting me, but that will not work!')
        print(f'Try again, sassy {player}, you!')
    elif int(guess_num) < true_num:
        print('Oh, too bad, you think too small!')
        print(f'Your guess of {guess_num} is smaller than my number.')
        print(f'Try again, {player}, if you\'re big enough.')
        guesses = guesses + 1
    elif int(guess_num) > true_num:
        print(f'Bold delusions of grandeur, {player}!')
        print(f'Your audacious suggestion of {guess_num} is far too large.')
        print('Try again, if you can rein yourself in.')
        guesses = guesses + 1
    elif int(guess_num) == true_num:
        print(f'Wow, {player}, good job. You have actually managed.')
        print(f'Now, admittedly, it took you {guesses} attempts, so.')
        print('I think we can all agree that I, a noble computer, remain the superior being.')
        print(f'Nontheless, {player}, thank you for playing with me. I would tolerate playing with you again soon.')
        break
    else:
        print('Honestly, I\'m boggled. What you done?!')
        print('Okay, let\'s try again.')
