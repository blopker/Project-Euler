cards = dict([(str(x),x) for x in range(2,10)])
cards['A'] = 14
cards['K'] = 13
cards['Q'] = 12
cards['J'] = 11
cards['T'] = 10

def royalflush(p1num):
  if flush(p1num) and straight(p1num) == 14:
    return straight(p1num)
  return False

def straightflush(p1num):
  if flush(p1num) and straight(p1num):
    return straight(p1num)
  return False

def fourkind(p1num):
  for num in p1num:
    if p1num.count(num) == 4:
      return num
  return False

def fullhouse(p1num):
  if threekind(p1num) and onepair(p1num):
    return [threekind(p1num),onepair(p1num)]
  return [0]

def flush(p1suit):
  if len(set(p1suit)) == 1:
    return True
  return False

def straight(pnum):
  p1num = pnum
  p1check = 0
  p1num.sort()
  for num in range(len(p1num)-1):
    if p1num[num] + 1 != p1num[num + 1]:
      return False
  return max(p1num)

def threekind(p1num):
  for num in p1num:
    if p1num.count(num) == 3:
      return num
  return False

def twopair(p1num):
  for num in p1num:
    if p1num.count(num) == 2:
      num1 = num
  for num in p1num:
    if p1num.count(num) == 2 and num != num1:
      num2 = num
      return num1,num2
  return False

def onepair(p1num):
  for num in p1num:
    if p1num.count(num) == 2:
      return num
  return False

def highcard(p1num):
  high = 0
  for num in p1num:
    if p1num.count(num) == 1 and num > high:
      high = num
  return high

def tupler(hand):
  return (hand[:2],hand[3:5],hand[6:8],hand[9:11],hand[12:-1])


with open("poker.txt") as f:
  wins = 0
  lose = 0
  for game in f.readlines():
    player1 = tupler(game[:15])
    player2 = tupler(game[15:])
    p1num = [cards[x] for x in [player1[x][0] for x in range(len(player1))]]
    p2num = [cards[x] for x in [player2[x][0] for x in range(len(player2))]]
    p1suit = [player1[x][1] for x in range(len(player1))]
    p2suit = [player2[x][1] for x in range(len(player2))]

    if royalflush(p1num) or royalflush(p2num):
      print player1,player2,'rf'
      wins += 1
    if straightflush(p1num) or straightflush(p2num):
      print player1,player2,'sf'
      wins += 1
    if fourkind(p1num) or fourkind(p2num):
      print player1,player2,'fk'
      if fourkind(p1num) > fourkind(p2num):
        wins += 1
      if fourkind(p1num) == fourkind(p2num):
        if highcard(p1num) > highcard(p2num):
          wins += 1
    if max(fullhouse(p1num)) or max(fullhouse(p2num)):
      #print player1,player2,"fh"
      continue
    if flush(p1suit) or flush(p2suit):
      #print player1,player2
      if flush(p1suit):
        wins += 1
      continue
    if straight(p1num) or straight(p2num):
      #print player1,player2,'s'
      if straight(p1num):
        wins+=1
      continue
    if threekind(p1num) or threekind(p2num):
      #print player1,player2,'tk'
      if threekind(p1num):
        wins+=1
      continue
    if twopair(p1num) or twopair(p2num):
      #print player1,player2,"tp",p1num,p2num
      if twopair(p1num):
        wins += 1
      continue
    if onepair(p1num) or onepair(p2num):
      #print player1,player2
      if onepair(p1num) > onepair(p2num):
        wins+=1
      if onepair(p1num) == onepair(p2num):
        if highcard(p1num) > highcard(p2num):
          wins+=1
      continue
    if highcard(p1num) or highcard(p2num):
      if highcard(p1num) > highcard(p2num):
        wins+=1
        continue
      if highcard(p1num) < highcard(p2num):
        continue
  print wins
    
    
