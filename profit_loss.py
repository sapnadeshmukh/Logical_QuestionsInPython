actual_cost = int(input(" Please Enter the Actual Product Price: "))
sale_amount = int(input(" Please Enter the Sales Amount: "))
 
if(actual_cost >sale_amount):
    amount = actual_cost - sale_amount
    print("Total Loss Amount ", amount)
elif(sale_amount > actual_cost ):
    amount = sale_amount - actual_cost
    print("Total Profit" ,amount)
else:
    print("No Profit No Loss!!!")