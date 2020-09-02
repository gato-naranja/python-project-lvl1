import random
from math import sqrt


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_question_and_answer():
    question = random.randint(1, 1000)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (str(question), correct_answer)
