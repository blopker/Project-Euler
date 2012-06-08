for x in range(1010101010,1389026623,10):
  check = x**2
  if str(check)[::2] == '1234567890':
    print x
