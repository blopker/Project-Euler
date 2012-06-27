import math
import fractions


def primitiveTriples(x):
    mx = int(.5 * (math.sqrt(2 * x + 1) - 1))
    for m in range(1, mx):
        for n in range(1, m):
            if m * (m + n) >= x / 2:
                break
            if fractions.gcd(m, n) == 1 and (m - n) % 2 == 1:
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                yield a, b, c

ans = {}
x = 1500000
for prim in primitiveTriples(x):
    s = sum(prim)
    k = 1
    n = k * s
    while n <= x:
        if not n in ans:
            ans[n] = 1
        else:
            ans[n] += 1
        k += 1
        n = k * s
count = 0
for k, v in ans.iteritems():
    if v == 1:
        count += 1
print count
