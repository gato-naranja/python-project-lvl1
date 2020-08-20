import random


GAME_RULE = 'Answer "yes" if number even otherwise answer "no".'


def calculation_values_game():
    num = random.randint(1, 100)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (num, correct_answer)
