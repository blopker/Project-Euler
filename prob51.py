import time
primes = frozenset([i.strip() for i in open("primes.txt").readlines()])


def dupDigits(prime):
    for s in ['0', '1', '2']:
        c = prime.count(s)
        if c > 2 and not prime[-1] == s:
            check(prime, s)


def check(prime, s):
    count = 0
    for x in "0123456789":
        if prime.replace(s, x) in primes:
            count += 1
    if count == 8:
        print prime, count

t1 = time.time()
for prime in primes:
    dupDigits(prime)
t2 = time.time()
print (t2 - t1)
