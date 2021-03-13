# logical question to print empty list and numbers

list1=[1,2,3,4]
i=0
sub=0
sublist=[]
while i<len(list1):
	j=0
	while j<(len(list1)+1):
		sub=list1[i:j]
		sublist.append(sub)
		j=j+1
	i=i+1
print (sublist)

