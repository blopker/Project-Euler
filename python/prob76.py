import euler
import itertools

t = set()
for perm in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    t.add(euler.listToInteger(perm))


def fibIterTruncate():
    a, b = 0, 1
    while 1:
        yield a
        a = a % 1000000000
        a, b = b, a + b


def check(i):
    l = i % 1000000000
    if l in t:
        f = euler.getFirstNDigits(i, 9)
        if f in t:
            return True
    return False

print check(123456789)

count = 0
for x in euler.fibIter():
    if check(x):
        print count
        break
    count += 1
