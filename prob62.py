import time
t = time.time()


def listToStr(lis):
    ans = ""
    for s in lis:
        ans += s
    return ans


d = {}
for num in range(300, 9000):
    num = num ** 3
    snum = listToStr(sorted(str(num)))
    if snum in d:
        d[snum][1] += 1
    else:
        d[snum] = [num, 1]
    if d[snum][1] == 5:
        print "answer:", d[snum][0]
        break
print time.time() - t
