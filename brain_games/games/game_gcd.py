import random


def get_devisor(n1, n2):
    if n1 % n2 == 0:
        return n2
    else:
        r = n1 - n2 * (n1 // n2)
        return get_devisor(n2, r)


def calculate_gcd(number_of_attempts):
    game_gcd_rule = 'Find the greatest common divisor of given numbers.'
    game_result = [game_gcd_rule]
    while number_of_attempts:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        if num2 > num1:
            (num1, num2) = (num2, num1)
        greatest_common_divisor = get_devisor(num1, num2)
        game_result.append((
            '{0} {1}'.format(num1, num2),
            str(greatest_common_divisor)
            ))
        number_of_attempts -= 1
    return game_result
