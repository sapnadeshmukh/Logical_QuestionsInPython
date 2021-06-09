list1=[1,2,3,4,6]
list2=["abhi","sap","pihu","kuki","lilo"]
i=0
c={}
while i<len(list1):
    if len(list1)==len(list2):
        c[list1[i]]=list2[i]
    else:
        j=0
        while (len(list1)==len(list2)):
            c[list1[j]]=list2[j]
        else:
            c[list1[j]]=list2[j]
        j=j+1


    i=i+1
print(c)
