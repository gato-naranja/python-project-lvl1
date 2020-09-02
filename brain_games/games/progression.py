import random


GAME_RULE = 'What number is missing in the progression?'


def generate_question_and_answer():
    # Formation of the progression and definition of a lost item
    PROGRESSION_LENGTH = 10
    progression_body = [random.randint(1, PROGRESSION_LENGTH)]
    question = ''
    step_progression = random.randint(1, 10)
    lost_item_index = random.randint(0, PROGRESSION_LENGTH - 1)
    i = 1
    while i < PROGRESSION_LENGTH:
        progression_body.append(progression_body[i - 1] + step_progression)
        i += 1
    for i in range(PROGRESSION_LENGTH):
        if i == lost_item_index:
            question += ' ..'
            correct_answer = str(progression_body[i])
        else:
            question += ' ' + str(progression_body[i])
    return (question, correct_answer)
