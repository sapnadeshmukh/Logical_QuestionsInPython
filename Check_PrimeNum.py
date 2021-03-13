result=0
user=int(input("enter num"))
i=1
while (i<=user):
    if user%i==0:
        result=result+1
    i=i+1
if result==2:
    
    print("prime")
else:
    print("not prime")