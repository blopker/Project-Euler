import fractions
import euler

limit = 15499 / 94744.0
print "Limit:", limit
# limit = 4 / 10.0
primes = euler.primes()

def check(x):
    count = 0
    for i in xrange(x):
        if fractions.gcd(i, x) == 1:
            count += 1
    return count


def check2(x):
    count = 1
    factors = []
    for prime in primes:
        if 2 * prime > x:
            break
        if x % prime == 0:
            count += x / prime
            count -= 1
            factors.append(prime)
    print factors
    for i in range(len(factors) - 1):
        for b in range(i + 1, len(factors)):
            c = factors[i] * factors[b]
            if x % c == 0:
                count -= x / c
                count += 1

    return x - count

# 1 2 1 0.836411804441
# 2 6 2 0.236411804441
# 8 30 4 0.112273873407
# 48 210 6 0.0660768762118
# 480 2310 10 0.0442940045281
# 5760 30030 12 0.0282263836815

# def test():
#     for x in range(100):
#         print check(x), check2(x)

# min = 1
# last = 0
# for x in xrange(60, 13000000, 30):
#     ans = check(x)
#     ratio = ans / float(x - 1)
#     if ratio < min:
#         min = ratio
#         print ans, x, x - last, min - limit
#         if min < limit:
#             print "WIN"
#         last = x


now = 1
lastans = 1
for p in primes[:6]:
    now *= p
    ans = check2(now)
    ratio = ans / float(now - 1)
    print ans, now, ans / lastans, ratio - limit
    lastans = ans
