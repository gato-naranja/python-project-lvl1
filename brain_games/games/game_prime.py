import random
from math import sqrt


def is_number_prime(number_of_attempts):
    game_even_rule = str(
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )
    game_result = [game_even_rule]
    while number_of_attempts:
        num = random.randint(1, 1000)
        sqrt_from_num = int(sqrt(num))
        correct_answer = 'yes'
        for i in range(2, sqrt_from_num + 1):
            if num % i == 0:
                correct_answer = 'no'
        game_result.append((str(num), correct_answer))
        number_of_attempts -= 1
    return game_result
