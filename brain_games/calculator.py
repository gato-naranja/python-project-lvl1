import prompt
from brain_games.cli import welcome_user
from brain_games.cli import incorrect_answer
from brain_games.games.game_calc import calc


def game_calculator():
    # Main func for game of calculator
    print('What is the result of the expression?')
    print()
    name = welcome_user()
    print()
    attempts = 3
    while attempts:
        result = calc()
        answer = prompt.integer('Your answer: ')
        if answer == result:
            print('Correct!')
            attempts -= 1
        else:
            incorrect_answer(name, answer, result)
            break
    if not attempts:
        print('Congratulations, {0}!'.format(name))
