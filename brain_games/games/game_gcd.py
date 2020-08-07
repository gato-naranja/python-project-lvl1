import random


def devisor(n1, n2):
    if n1 % n2 == 0:
        return n2
    else:
        r = n1 - n2 * (n1 // n2)
        return devisor(n2, r)


def gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print('Question: {0} {1}'.format(num1, num2))
    if num2 > num1:
        (num1, num2) = (num2, num1)
    return devisor(num1, num2)
