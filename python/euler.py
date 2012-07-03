import math
import fractions


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

# from http://en.literateprograms.org/Fibonacci_numbers_(Python)
fibs = {0: 0, 1: 1}


def fib(n):
    if n in fibs:
        return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
        return fibs[n]
    else:
        fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n + 1) / 2) ** 2)
        return fibs[n]


def fibIter():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b


def getFirstNDigits(x, n):
    """ gets first n digits of an integer """
    while x > 10 ** n:
        x /= 10
    return x


def listToInteger(lis):
    l = len(lis) - 1
    n = 0
    for i in lis:
        n += int(i) * 10 ** l
        l -= 1
    return n


def readGraph(file):
    """For reading graphs like in problem 81"""
    ls = []
    with open(file) as f:
        for line in f:
            ls.append([int(x) for x in line.split(",")])
    return ls


def totient(n):
    """
    count totatives of n, assuming gcd already
    defined
    """
    tot, pos = 1, n - 1
    while pos > 1:
        if fractions.gcd(pos, n) == 1:
            tot += 1
        pos -= 1
    return tot
