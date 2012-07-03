#Also, fib(32) is the correct answer.
count = 0
for n in xrange(1,2**30+1):
  if not n^(2*n)^(3*n):
    count+=1
    #print bin(n),bin(n*2),bin(n*3)
print count
