import random


def generate_calculator():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    symbol_operation = random.randint(1, 3)
    if symbol_operation == 1:
        operation_result = num1 + num2
        print('Question: {0}+{1}'.format(num1, num2))
    elif symbol_operation == 2:
        operation_result = num1 - num2
        print('Question: {0}-{1}'.format(num1, num2))
    else:
        operation_result = num1 * num2
        print('Question: {0}*{1}'.format(num1, num2))
    return operation_result
