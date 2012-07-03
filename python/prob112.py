flag = True
total = 10
bounce = 0.0

def isdown(num):
  stri = str(num)
  for x in range(len(stri)-1):
    if int(stri[x]) < int(stri[x+1]):
      return False
  return True

def isupp(num):
  stri = str(num)
  for x in range(len(stri)-1):
    if int(stri[x]) > int(stri[x+1]):
      return False
  return True

def isbouncy(num):
  if not isdown(num) and not isupp(num): return True
  else: return False

while flag:
  if isbouncy(total):
    bounce +=1
  if bounce/total == .99:
    print bounce,total
    break
    flag = False
  if total == 1000:
    print bounce

  total += 1
