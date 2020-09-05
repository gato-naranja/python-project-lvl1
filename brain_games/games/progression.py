import random


GAME_RULE = 'What number is missing in the progression?'


def generate_question_and_answer():
    # Formation of the progression and definition of a lost item
    PROGRESSION_LENGTH = 10
    first_elem = random.randint(1, PROGRESSION_LENGTH)
    step_progression = random.randint(1, 10)
    end_elem = first_elem + step_progression * PROGRESSION_LENGTH
    lost_item_index = random.randint(0, PROGRESSION_LENGTH - 1)
    progression_body = list(
        map(
            str,
            range(first_elem, end_elem, step_progression)
            )
        )
    for i in range(PROGRESSION_LENGTH):
        if i == lost_item_index:
            correct_answer = progression_body[i]
            progression_body[i] = '..'
            break
    question = ' '.join(progression_body)
    return (question, correct_answer)
