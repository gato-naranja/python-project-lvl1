import random


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_devisor(n1, n2):
    if n1 % n2 == 0:
        return n2
    else:
        r = n1 - n2 * (n1 // n2)
        return get_devisor(n2, r)


def calculation_values_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    if num2 > num1:
        (num1, num2) = (num2, num1)
    return ('{0} {1}'.format(num1, num2), str(get_devisor(num1, num2)))
