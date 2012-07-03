def pancheck(n):
  setn = {x for x in n}
  if len(setn) == len(n):
    return True
  else:
    return False

i = 1023456789
while i > 0:
  i = str(i)
  if pancheck(i) == True and len(i) == 10:
    if int(i[7]+i[8]+i[9]) % 17 == 0:
      if int(i[2]+i[3]+i[4]) % 3 == 0:
        if int(i[3]+i[4]+i[5]) % 5 == 0:
          if int(i[4]+i[5]+i[6]) % 7 == 0:
            if int(i[5]+i[6]+i[7]) % 11 == 0:
              if int(i[6]+i[7]+i[8]) % 13 == 0:
                if int(i[1]+i[2]+i[3]) % 2 == 0:
                  print(i)
  print(i[0])
  i = int(i)
  i += 1
