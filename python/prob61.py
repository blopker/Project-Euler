from itertools import permutations

def p3(n):
    return n*(n+1)/2

def p4(n):
    return n**2

def p5(n):
    return n*(3*n-1)/2

def p6(n):
    return n*(2*n-1)

def p7(n):
    return n*(5*n-3)/2

def p8(n):
    return n*(3*n-2)

def generate_all_fours(func):
    n = 0
    while func(n) < 1000:
        n = n + 1
    four = func(n)
    while four < 10000:
        yield four
        n = n + 1
        four = func(n)

def prefix(n):
    return n/100

def postfix(n):
    return n%(n/100*100)

# Generate a prefix hash for quickly finding numbers.
funcs = [p3, p4, p5, p6, p7, p8]
# funcs = [p3, p4, p5]
pre = []
for func in funcs:
    dic = {}
    for four in generate_all_fours(func):
        dic.setdefault(prefix(four),[]).append(four)
    pre.append(dic)

answer = []

def find_next_four(fours, fours_pool):
    if len(fours) == len(funcs) and prefix(fours[0]) == postfix(fours[-1]):
        answer.append(fours)
    if fours_pool == []:
        return 
    for four in fours_pool.pop().get(postfix(fours[-1]), []):
        new_fours = list(fours)
        new_fours.append(four)
        find_next_four(new_fours, fours_pool)

for fours_pool in permutations(pre):
    if answer: break
    fours_pool = list(fours_pool)
    start = [four for x in fours_pool.pop().values() for four in x]

    for four in start:
        find_next_four([four], list(fours_pool))
        
print sum(answer[0])