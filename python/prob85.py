maxx, highest = 1999, 0
for row in reversed(range(maxx)):
  for col in range(maxx):
    r = .25*col*row*(col+1)*(row+1)
    if r > highest and r < 2000000:
      highest = r
      print row*col
    if r > 2000000:
      break
