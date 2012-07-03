#'end' is the nth term needed.
count, k, top1, top2, end = 0, 2, 8, 3, 100
for num in xrange(2,end-1):
  if count == 2:
    top1, top2 = top1*2*k+top2, top1
    count = 0
    k += 1
  else:
    top1, top2 = top1+top2, top1
    count += 1
print sum([int(x) for x in list(str(top1))])
    
