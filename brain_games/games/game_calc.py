import random


def calc():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.randint(1, 3)
    if operation == 1:
        result = num1 + num2
        print('Question: {0}+{1}'.format(num1, num2))
    elif operation == 2:
        result = num1 - num2
        print('Question: {0}-{1}'.format(num1, num2))
    else:
        result = num1 * num2
        print('Question: {0}*{1}'.format(num1, num2))
    return result
