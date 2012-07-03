#http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

from math import floor
from itertools import repeat
count = 0
for s in xrange(10000):
  ite, m, d = 0, 0, 1
  a0 = floor(s**.5)
  a = a0
  while True:
    m = d*a - m
    d = (s - m**2)/d
    if d == 0:
      break
    a = floor((a0+m)/d)
    if s < a**2:
      if (ite%2==0): #test if sequence is odd
        count += 1
      break
    ite += 1
print count
