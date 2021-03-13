a=["sapna",2,"jyoti",3,2.3,"abhi",4]
i=0
new=[]
while i<len(a):
    c=type(a[i])
    if c==str:
        new.append("str")
    if c==float:
        new.append("float")
    if c==int:
        d=a[i]*a[i]
        new.append(d)
    i=i+1
print(new)
