    # position of prime number

number=int(input("enter num"))
position=0
index=1
while index<=number:
    count=0
    j=2
    while j<=index:
        if index%j==0:
            count=count+1
        j=j+1
    if count==1:
        position=position+1
        if index==number:
            print("position is prime num is=",position)
        
    
    index=index+1