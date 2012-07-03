##for num in xrange(1,1000000):
##  lis = [num]
##  nex = fact(num)
##  while True:
##    if nex in lis:
##      if len(lis) == 60:
##        print lis[:6]
##      break
##    else:
##      lis.append(nex)
##    nex = fact(nex)

##[392742, 367954, 368790, 408967, 408985, 443665]
##[394227, 367954, 368790, 408967, 408985, 443665]
##[394272, 367954, 368790, 408967, 408985, 443665]
##[394722, 367954, 368790, 408967, 408985, 443665]
##[397224, 367954, 368790, 408967, 408985, 443665]
##[397242, 367954, 368790, 408967, 408985, 443665]
##[397422, 367954, 368790, 408967, 408985, 443665]

from math import factorial

def fact(num):
  nummer, summ = str(num), 0
  for didg in nummer:
    summ += factorial(int(didg))
  return summ

count = 0
b = list('367954')
b.sort()
for num in xrange(1,1000000):
  a = list(str(fact(num)))
  a.sort()
  if a == b:
    count += 1
print count
