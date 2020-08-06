# Command line interface for brain-games.


import prompt


def welcome_user():
    # Get an user name and promt user.:
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def incorrect_answer(user, answer, result):
    # Output message when answer is incorrect
    print(
            '\'{0}\' is wrong answer ;(. Correct answer was \'{1}\''
            .format(answer, result)
            )
    print('Let\'s try again, {0}!'.format(user))
