import random
import operator


GAME_RULE = 'What is the result of the expression?'


def calculation_values_game():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    symbol_operation = random.choice(('+', '-', '*'))
    if symbol_operation == '+':
        operation_result = operator.add(num1, num2)
    elif symbol_operation == '-':
        operation_result = operator.sub(num1, num2)
    else:
        operation_result = operator.mul(num1, num2)
    return (str(num1) + symbol_operation + str(num2), str(operation_result))
