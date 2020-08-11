# Command line interface for brain-games.


import prompt


def welcome_user():
    # Get an user name and promt user.:
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def print_rules(game):
    # Print rules for each selected game.
    if game == 'even':
        print('Answer "yes" if number even otherwise answer "no".')
    elif game == 'calc':
        print('What is the result of the expression?')
    elif game == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game == 'progression':
        print('What number is missing in the progression?')
    elif game == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    else:
        print('I don\'t play that game!')


def show_mess_when_incorrect_answer(user, answer, result):
    # Output message when answer is incorrect
    print(
            '\'{0}\' is wrong answer ;(. Correct answer was \'{1}\''
            .format(answer, result)
            )
    print('Let\'s try again, {0}!'.format(user))
