import math
import euler
from itertools import permutations

def is_tri(n):
    a = math.sqrt(3 * n + 1)
    if ((1 - a) / 3.0) % 1 == 0 or ((1 + a) / 3.0) % 1 == 0:
        return True
    return False


def is_square(n):
    a = math.sqrt(3 * n + 1)
    if ((1 - a) / 3.0) % 1 == 0 or ((1 + a) / 3.0) % 1 == 0:
        return True
    return False


def is_pent(n):
    a = math.sqrt(24 * n + 1)
    if ((1 - a) / 6.0) % 1 == 0 or ((1 + a) / 6.0) % 1 == 0:
        return True
    return False


def is_hex(n):
    a = math.sqrt(8 * n + 1)
    if ((1 - a) / 4.0) % 1 == 0 or ((1 + a) / 4.0) % 1 == 0:
        return True
    return False


def is_hep(n):
    a = math.sqrt(40 * n + 9)
    if ((3 - a) / 10.0) % 1 == 0 or ((3 + a) / 10.0) % 1 == 0:
        return True
    return False


def is_oct(n):
    a = math.sqrt(3 * n + 1)
    if ((1 - a) / 3.0) % 1 == 0 or ((1 + a) / 3.0) % 1 == 0:
        return True
    return False


def check(num, l):
    for end in range(10, 100):
        n = (num - num / 100 * 100) * 100 + end
        if n in l:
            return True
    return False
# for a in range(1000, 9999):
#     if is_oct(a):
#         for b in range(10, 100):
#             euler.concat_numbers(a / 100, b)
tri = set([x for x in range(1000, 9999) if is_tri(x)])
sq = set([x for x in range(1000, 9999) if is_square(x)])
pen = set([x for x in range(1000, 9999) if is_pent(x)])
hex = set([x for x in range(1000, 9999) if is_hex(x)])
hep = set([x for x in range(1000, 9999) if is_hep(x)])
oct = set([x for x in range(1000, 9999) if is_oct(x)])

ll = permutations([oct, hep, hex, pen, sq, tri], 6)
for l in ll:
    for a in l[0]:
        if check(a, l[1]):
            for b in l[1]:
                if check(b, l[2]):
                    for c in l[2]:
                        if check(c, l[3]):
                            for d in l[3]:
                                if check(d, l[4]):
                                    for e in l[4]:
                                        if check(e, l[5]):
                                            for f in l[5]:
                                                print a, b, c, d, e, f
