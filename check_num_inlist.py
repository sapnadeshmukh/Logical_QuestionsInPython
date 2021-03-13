# ask user for list and ask for number and check number is already exits in list or not
user=int(input("enter a number"))
i=0
new_list=[]
while i<user:
	value=int(input("enter value"))
	new_list.append(value)
	i=i+1
print (new_list)
user_ask=int(input("give again any number"))
if user_ask in new_list:
	print("your number is our list")
else:
	print ("your number is not in list")