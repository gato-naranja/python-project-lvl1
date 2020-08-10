import random


def progression():
    # Formation of the progression and definition of a lost item
    list = [random.randint(1, 10)]
    step = random.randint(1, 10)
    lostitemindex = random.randint(1, 10)
    i = 1
    while i < 10:
        list.append(list[i - 1] + step)
        i += 1
    lostitem = list[lostitemindex - 1]
    list[lostitemindex - 1] = '..'
    print('Question: ', *list)
    return lostitem
