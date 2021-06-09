def prime(num):
    index=2
    while index<=num:
        count=0
        j=2
        while j<index:
            if index%j==0:
                count=count+1
            j+=1
        if count==0:
            print(index)
    
        index+=1
num=int(input("enter range of Number:----"))
prime(num)

