from typing import Mapping


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)

def trailingZero(number):
    pass

if __name__ == '__main__':
    n = int(input("Give number: "))
    fact = factorial(n)
    print(fact)