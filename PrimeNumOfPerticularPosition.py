number=int(input("enter num"))
position=0
index=1
while True:
    count=0
    j=2
    while j<=index:
        if index%j==0:
            count=count+1
        j=j+1
    if count==1:
        position=position+1
        if position==number:
            print("prime num is=",index)
            break
        
    index=index+1