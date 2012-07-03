look = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,
        'I':1,'R':400,'T':900,'Y':40,'U':90,'O':4,'P':9,'\n':0}
lis = [('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),
        ('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
dubr = ['R','T','Y','U','O','P']
dub = ['CD','CM','XL','XC','IV','IX']
count = 0
with open('roman.txt') as nu:
  for lineo in nu.readlines():
    summ = 0
    lineo = lineo.replace('\n','')
    line = lineo
    linen = ''
    for x in dub:
      line = line.replace(x,dubr[dub.index(x)])
    for x in line:
      summ += look[x]
    for tup in lis:
      while summ >= tup[1]:
        linen += tup[0]
        summ -= tup[1]
    count += len(lineo)-len(linen)
print count
    
