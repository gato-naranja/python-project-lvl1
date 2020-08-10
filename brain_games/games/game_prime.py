import random


def prime():
    prime_list = (
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
            )
    number = random.randint(1, 100)
    print('Question: {0}'.format(number))
    if number in prime_list:
        return 'yes'
    else:
        return 'no'
