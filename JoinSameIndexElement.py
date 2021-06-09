list1=["m","na","i","ke"]
list2=["y","me","s","lly"]
newlist=[]
index=0
while index<len(list1):
    temp=list1[index]+list2[index]
    newlist.append(temp)
    index=index+1
print(newlist)