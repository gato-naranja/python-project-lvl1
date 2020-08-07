import prompt
from brain_games.cli import welcome_user
from brain_games.cli import incorrect_answer
from brain_games.games.game_gcd import gcd


def game_gcd():
    # Main func for game of greatest common divisor
    print('Find the greatest common divisor of given numbers.')
    print()
    name = welcome_user()
    print()
    attempts = 3
    while attempts:
        result = gcd()
        answer = prompt.integer('Your answer: ')
        if answer == result:
            print('Correct!')
            attempts -= 1
        else:
            incorrect_answer(name, answer, result)
            break
    if not attempts:
        print('Congratulations, {0}!'.format(name))
