import random


GAME_RULE = 'Answer "yes" if number even otherwise answer "no".'


def generate_question_and_answer():
    question = random.randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question, correct_answer)
