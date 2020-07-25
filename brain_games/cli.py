# Command line interface for brain-games.


import prompt


def welcome_user():
    # Get an user name and promt user.:
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
