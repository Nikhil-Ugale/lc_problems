def pascalTriangle(n):
  l=[]
  if n==1:
    return [[1]]
  else:
    l.append([1])
    for i in range(1,n):
      x = []
      x.append(1)
      for j in range(1,i):
        x.append(l[-1][j-1]+l[-1][j])
      x.append(1)
      l.append(x)
    return l

