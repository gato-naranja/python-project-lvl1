import random


def is_number_prime():
    prime_list = (
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
            )
    num = random.randint(1, 100)
    print('Question: {0}'.format(num))
    if num in prime_list:
        return 'yes'
    else:
        return 'no'
