user=int(input("enter number:--"))
main=[]
i=0
while i<user:
    num=int(input("enter num:-"))
    main.append(num)
    i=i+1
print(main)
sum=0
index=0
av=0
count=0
while index<len(main):
    sum=sum+main[index]
    count=count+1
    index=index+1
print(sum)
print(count)
print(sum%count)

print("*****************************************")

user=int(input("enter how may times:--"))
i=0
while i<user:
    user1=int(input("how many elements:--"))
    main=[]
    j=0
    while j<user1:
        give=int(input("enter num:-"))
        main.append(give)
        j=j+1
    print(main)
    sum=0
    index=0
    av=0
    count=0
    while index<len(main):
        sum=sum+main[index]
        count=count+1
        index=index+1

    print(sum)
    print(count)
    print(sum%count)
    i=i+1



