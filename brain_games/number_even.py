# set of functions for game of number even


import prompt
from brain_games.cli import welcome_user
from brain_games.cli import incorrect_answer
from brain_games.games.game_even import even


def game_even():
    # main func which generates numbers
    # then reading answers
    # and define that answer correct or no
    print('Answer "yes" if number even otherwise answer "no".')
    print()
    name = welcome_user()
    print()
    attempts = 3  # current number of questions for a successful game
    while attempts:
        result = even()
        answer = prompt.string('Your anser:')
        if answer == result:
            print('Correct!')
            attempts -= 1
        else:
            incorrect_answer(name, answer, result)
            break
    if not attempts:
        print('Congratulations, {0}!'.format(name))
