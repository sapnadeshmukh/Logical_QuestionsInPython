
a=["A","B"]
user=int(input("enter a number:---"))
i=1
new=[]
while (i<=user):
    j=0
    while(j<len(a)):
        new.append(a[j]+str(i))
        j=j+1
    i=i+1
print(new)
