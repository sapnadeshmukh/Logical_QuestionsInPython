# to print all elements of nested list
a=[[5,6,7],[1,5,6,7,8,0]]
i = 0
while i<len(a):
  j = 0
  while j < len(a[i]):
    print (a[i][j])
    j = j+1
  i = i+1