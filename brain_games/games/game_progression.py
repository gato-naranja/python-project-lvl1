import random


def ask_progression_task():
    # Formation of the progression and definition of a lost item
    list_numbers = [random.randint(1, 10)]
    step = random.randint(1, 10)
    lost_item_index = random.randint(0, 9)
    i = 1
    while i < 10:
        list_numbers.append(list_numbers[i - 1] + step)
        i += 1
    lost_item = list_numbers[lost_item_index]
    list_numbers[lost_item_index] = '..'
    print('Question: ', *list_numbers)
    return lost_item
