#!/usr/bin/env python
from itertools import permutations
import euler

primes = euler.primes()
primess = frozenset(primes)


def check(iter):
    for pair in iter:
        p1 = primes[pair[0]]
        p2 = primes[pair[1]]
        if not euler.isprime(euler.concat(p1, p2)):
            return False
        if not euler.isprime(euler.concat(p2, p1)):
            return False
    return True

pl = 1229  # check up to 4 digit primes.
for a in range(1, pl):
    for b in range(a, pl):
        if check(permutations([a, b], 2)):
            for c in range(b, pl):
                if check(permutations([a, b, c], 2)):
                    for d in range(c, pl):
                        if check(permutations([a, b, c, d], 2)):
                            for e in range(d, pl):
                                if check(permutations([a, b, c, d, e], 2)):
                                    print primes[a], primes[b], primes[c], primes[d], primes[e]
                                    print sum([primes[a], primes[b], primes[c], primes[d], primes[e]])
