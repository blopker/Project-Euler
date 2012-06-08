#Euler 38

def pancheck(n):
  for x in n:
    if x == '0':
      return False
  setn = {x for x in n}
  if len(setn) == len(n):
    return True
  else:
    return False

for i in range(1,10000):
  tot = ''
  mult = 1
  while len(tot) < 9:
    prod = i*mult
    tot += str(prod)
    mult += 1
  if len(tot) == 9 and pancheck(tot) == True:
    print(tot)
    
