import random


def even():
    num = random.randint(1, 100)
    print('Question: {0}'.format(num))
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'
