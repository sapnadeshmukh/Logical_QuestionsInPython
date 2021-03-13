column=int(input("enter column:-"))
row=int(input("enter rows:-"))
i=1
small_list=[]
while (i<=row):
    big_list=[]
    j=1
    k=0
    while(j<=column):
        k=i*j
        big_list.append(k)
        j=j+1

    i=i+1
    small_list.append(big_list)

print(small_list)


    