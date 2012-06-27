import math


def primes():
    primes = []
    with open("primes.txt") as p:
        for line in p:
            primes.append(int(line.strip()))
    return primes


def isprime(number):
    if number <= 1 or number % 2 == 0:
        return False
    for check in range(3, int(math.sqrt(number)) + 1, 2):
        if number % check == 0:
            return False
    return True


def concat_numbers(n1, n2):
    for i in range(20):
        if n2 / 10 ** i == 0:
            n1 = n1 * 10 ** i
            return n1 + n2
