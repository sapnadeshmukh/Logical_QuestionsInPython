unit=int(input("enter unit"))
if unit<=50:
	amount =unit*0.50
	print (amount)
elif unit>50 and unit<=150:
	amount=unit*0.75
	print (amount)
elif unit>150 and unit<=250:
	amount=unit*1.20
	print (amount)
elif unit>250:
	amount=unit*1.50
	print (amount)
sur_charge=amount*20/100
total_amount=amount+sur_charge
print ("electric bill will be",total_amount)