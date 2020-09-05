import random


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_gcd(n1, n2):
    if n2 > n1:
        (n1, n2) = (n2, n1)
    if n1 % n2 == 0:
        return n2
    else:
        r = n1 - n2 * (n1 // n2)
        return get_gcd(n2, r)


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    numbers_for_question = str(num1) + ' ' + str(num2)
    return (numbers_for_question, str(get_gcd(num1, num2)))
