user=int(input("enter a number of elements in list:---"))
solders=[]
i=1
while i<=user:
    people=int(input("enter num:--"))
    solders.append(people)
    i=i+1
print(solders)
count_even=0
count_odd=0
i=0
while i<len(solders):
    if solders[i]%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
    i=i+1
print(count_even)
print(count_odd)
if count_even >count_odd:
    print("Ready for war!!!")
else:
    print("Not Ready")
