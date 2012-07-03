def area(A,B,C):
  return abs((A[0]*1.0*(B[1]-C[1])+B[0]*(C[1]-A[1])+C[0]*(A[1]-B[1]))/2)


with open('triangles.txt') as f:
  count = 0
  for points in f.readlines():
    triangle = eval(points)
    p1 = triangle[:2]
    p2 = triangle[2:4]
    p3 = triangle[4:]
    a1 = area(p1,p2,p3)
    a2 = area(p1,p2,(0,0))
    a3 = area(p1,p3,(0,0))
    a4 = area(p3,p2,(0,0))
    if a1 == (a2+a3+a4):
      count += 1
  print count
