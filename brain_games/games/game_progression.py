import random


def ask_progression_task(number_of_attempts):
    # Formation of the progression and definition of a lost item
    game_even_rule = 'What number is missing in the progression?'
    game_result = [game_even_rule]
    while number_of_attempts:
        PROGRESSION_LENGTH = 10
        progression_body = [random.randint(1, 10)]
        progression_string = ''
        step_progression = random.randint(1, 10)
        lost_item_index = random.randint(0, 9)
        i = 1
        while i < PROGRESSION_LENGTH:
            progression_body.append(progression_body[i - 1] + step_progression)
            i += 1
        for i in range(PROGRESSION_LENGTH):
            if i == lost_item_index:
                progression_string += ' ..'
                lost_item = str(progression_body[i])
            else:
                progression_string += ' ' + str(progression_body[i])
        game_result.append((progression_string, lost_item))
        number_of_attempts -= 1
    return game_result
