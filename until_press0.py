i = 0
sum = 0
product = 1
while True:
	m = int(input("ask user to press 0 after every integer :"))
	if m == 0 :
		break
	else:
		sum = sum+m
		product = product *m
print("sum : ",sum)
print("Product of all the numbers :",product)