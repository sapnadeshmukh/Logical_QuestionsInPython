i=0
new=[]
while i<10:
    num=int(input("enter num"))
    new.append(num)

    if new[i]%2==0:
        print(new[i]*100)
    else:
        print(new[i]*-1)
    
    i=i+1