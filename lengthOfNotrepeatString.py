
        # By using Loop
a=input("enter any string")
i=0
new_list=[]
while (i<len(a)):
    if a[i] not in new_list:
        new_list.append(a[i])
    i=i+1

print(len(new_list))



print("************************************")
            #by function
def checkDuplicate(a):
    i=0
    new_list=[]
    while (i<len(a)):
        if a[i] not in new_list:
            new_list.append(a[i])
        i=i+1
    return (len(new_list))

user=input("enter any string")
print(checkDuplicate(user))





    
