import prompt
from brain_games.cli import welcome_user
from brain_games.cli import incorrect_answer
from brain_games.games.game_progression import calc_progression


def game_progression():
    # Main func for game of progression
    print('What number is missing in the progression?')
    print()
    name = welcome_user()
    print()
    attempts = 3
    while attempts:
        result = calc_progression()
        answer = prompt.integer('Your answer: ')
        if answer == result:
            print('Correct!')
            attempts -= 1
        else:
            incorrect_answer(name, answer, result)
            break
    if not attempts:
        print('Congratulations, {0}!'.format(name))
