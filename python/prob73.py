# using Farey sequences (https://en.wikipedia.org/wiki/Farey_sequence)


def farey(n):
    a, b, c, d = 0, 1, 1, n
    while c <= n:
        k = (n + b) / d
        a, b, c, d = c, d, k * c - a, k * d - b
        yield (a, b)

count = 0
start = False
for frac in farey(12000):
    if frac == (1, 2):
        break
    if start:
        count += 1
    if frac == (1, 3):
        start = True

print count
