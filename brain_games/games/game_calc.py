import random


def generate_calculator(number_of_attempts):
    game_calculator_rule = 'What is the result of the expression?'
    game_result = [game_calculator_rule]
    while number_of_attempts:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        symbol_operation = random.randint(1, 3)
        if symbol_operation == 1:
            operation_result = num1 + num2
            expression_for_solution = '{0}+{1}'.format(num1, num2)
        elif symbol_operation == 2:
            operation_result = num1 - num2
            expression_for_solution = '{0}-{1}'.format(num1, num2)
        else:
            operation_result = num1 * num2
            expression_for_solution = '{0}*{1}'.format(num1, num2)
        game_result.append((expression_for_solution, str(operation_result)))
        number_of_attempts -= 1
    return game_result
