#Euler prob 32

def pancheck(n):
  for x in n:
    if x == '0':
      return False
  setn = {x for x in n}
  if len(setn) == len(n):
    return True
  else:
    return False


sett = set()
for i in range(1,100000):
  w = 1
  tot = ''
  while len(tot) < 10:
    tot = str(i) + str(w) + str(i*w)
    if len(tot) == 9 and pancheck(tot) == True:
      sett.add(i*w)
    w += 1

l = 0
for x in sett:
  l += x
print(l)
