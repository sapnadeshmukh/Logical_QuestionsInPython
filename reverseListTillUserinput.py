list=[1,4,6,7]
user=int(input("enter a nub:-"))
l=len(list)-1
i=0
new=[]
while i<(user):
    new.append(list[l])
    l=l-1
    i=i+1
print(new)


