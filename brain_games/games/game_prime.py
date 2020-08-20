import random
from math import sqrt


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def calculation_values_game():
    num = random.randint(1, 1000)
    if is_prime(num):
        return (str(num), 'yes')
    return (str(num), 'no')
