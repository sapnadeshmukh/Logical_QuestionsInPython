# take list of numbers and reverse it in list
user=int(input("enter a number"))
i=0
new_list=[]
while i<user:
	value=int(input("enter value"))
	new_list.append(value)
	i=i+1
print (new_list)
new_list.reverse()
print (new_list)