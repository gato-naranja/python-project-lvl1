import random


def ask_even_number(number_of_attempts):
    game_even_rule = 'Answer "yes" if number even otherwise answer "no".'
    game_result = [game_even_rule]
    while number_of_attempts:
        num = random.randint(1, 100)
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        game_result.append((num, correct_answer))
        number_of_attempts -= 1
    return game_result
