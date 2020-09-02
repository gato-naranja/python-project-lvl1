import random
import operator


GAME_RULE = 'What is the result of the expression?'


def generate_question_and_answer():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operations = ['+', '-', '*']
    operation_symbol = random.choice(operations)
    if operation_symbol == '+':
        operation_result = operator.add(num1, num2)
    elif operation_symbol == '-':
        operation_result = operator.sub(num1, num2)
    elif operation_symbol == '*':
        operation_result = operator.mul(num1, num2)
    question = str(num1) + operation_symbol + str(num2)
    return (question, str(operation_result))
