# ask numbers of number and check how many numbers are positive,negative,odd,even,"0s" and contains it in list and show that list
user=int(input("enter input"))
i=0
a=[]
b=[]
c=[]
d=[]
e=[]
while i<user:
	user_input=int(input("enter value"))
	if user_input==0:
		e.append(user_input)
	if user_input > 0:
		a.append(user_input)
	if user_input<0:
		b.append(user_input)
	if user_input%2==0:
		c.append(user_input)
	if user_input%2!=0:
		d.append(user_input)
	i=i+1
print ("number of positive numbers",a)
print ("number of negative numbers",b)
print ("number of even numbers",c)
print ("number of odd numbers",d)
print ("number of 0s",e)