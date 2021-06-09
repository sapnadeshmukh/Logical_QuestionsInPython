

str1 = "sapna"

str_dict = {}
for i in str1:
    str_dict[i] = str1.count(i)
print(str_dict)


##without using count :
a="w3resource"
b=[]
y=[]
d=[]
s=[]
x={}
for q in a:
    b.append(q)
i=0
while i<len(b):
    j=0
    c=0
    while j<len(b):
        if b[i]==b[j]:
            y.append(b[i])
            c+=1
        j+=1
    k=0
    while k<1:
        if b[i] not in d:
            d.append(b[i])
            s.append([b[i],c])
            x.update(s)
        k+=1
    i+=1
print(x)

#3with using count:
a="w3resource"
b=[]
x={}
for i in a:
    b.append(i)
    y=b.count(i)
    x.update({i:y})
print(x)