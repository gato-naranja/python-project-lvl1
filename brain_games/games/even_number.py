import random


GAME_RULE = 'Answer "yes" if number even otherwise answer "no".'


def generate_question_and_answer():
    number_for_question = random.randint(1, 100)
    if number_for_question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (number_for_question, correct_answer)
