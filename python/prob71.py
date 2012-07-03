limit = 1000000
for x in reversed(range(0,limit+1)):
  if x%7 == 5:
    print ((x-5)/7)*3+2
    break


##best = 0
##for ed in range(300):
##  lower = 0
##  for d in range(ed+1):
##    for n in range(d):
##      guess = Fraction(n,d)
##      if guess <= lower:
##        continue
##      if guess >= Fraction(3,7):
##        continue
##      lower = guess
##  if lower > best:
##    best = lower
##    print ed,is_prime(ed),best,is_prime(best.numerator),is_prime(best.denominator)
