#Euler 41

def isprime(n):
    n*=1.0
    if n%2==0 and n!=2 or n%3==0 and n!=3:
        return False
    for b in range(1,int((n**0.5+1)/6.0+1)):
        if n%(6*b-1)==0:
            return False
        if n %(6*b+1)==0:
           return False
    return True
  
def pancheck(n):
  n = str(n)
  for x in n:
    if x == '0' or int(x) > len(n):
      return False
  setn = {x for x in n}
  if len(setn) == len(n):
    return True
  else:
    return False

  
for x in range(10000000,1000000,-1):
  if pancheck(x) == True and isprime(x) == True:
    print(x)
    break
