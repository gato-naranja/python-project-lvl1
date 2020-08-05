# set of functions for game of number even


import prompt
import random


def correct_answer(item):
    # returning the correct answer for random number - even or no
    if item % 2 == 0:
        return 'yes'
    if item % 2 != 0:
        return 'no'


def game_even(name):
    # main func which generates numbers
    # then reading answers
    # and define that answer correct or no
    attempts = 3  # current number of questions for a successful game
    while attempts:
        choise = random.randint(1, 100)
        print('Question:', choise)
        answer = prompt.string('Your anser:')
        if answer == correct_answer(choise):
            print('Correct!')
            attempts -= 1
        else:
            print(
                    '\''
                    + answer +
                    '\' is wrong answer ;(. Correct answer was \''
                    + correct_answer(choise) +
                    '\''
                    )
            print('Let\'s try again, {0}!'.format(name))
            break
    if not attempts:
        print('Congratulations, {0}!'.format(name))
