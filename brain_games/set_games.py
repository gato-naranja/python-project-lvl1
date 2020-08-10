import prompt
from brain_games.cli import welcome_user
from brain_games.cli import rules
from brain_games.cli import incorrect_answer
from brain_games.games.game_even import even
from brain_games.games.game_gcd import gcd
from brain_games.games.game_calc import calc
from brain_games.games.game_progression import progression
from brain_games.games.game_prime import prime


def brain_game(game):
    # In the argument 'game' should be one of following values:
    #   even - for game of number even;
    #   gcd - for game of greatest common divisor;
    #   calc - for game of calculator;
    #   progression - for game of progression;
    #   prime for game of prime number.
    rules(game)
    print()
    name = welcome_user()
    print()
    attempts = 3
    while attempts:
        if game == 'even':
            result = even()
            answer = prompt.string('Your answer: ')
        elif game == 'gcd':
            result = gcd()
            answer = prompt.integer('Your answer: ')
        elif game == 'calc':
            result = calc()
            answer = prompt.integer('Your answer: ')
        elif game == 'progression':
            result = progression()
            answer = prompt.integer('Your answer: ')
        elif game == 'prime':
            result = prime()
            answer = prompt.string('Your answer: ')
        else:
            return print('Sorry, {0}!'.format(name))
        if answer == result:
            print('Correct!')
            attempts -= 1
        else:
            incorrect_answer(name, answer, result)
            break
    if not attempts:
        print('Congratulations, {0}!'.format(name))
