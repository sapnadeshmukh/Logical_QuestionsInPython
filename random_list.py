import random
num=int(input("enter how many elements:-"))
new=[]
i=1
while i<=num:

    new.append(i)
    i=i+1
print(new)
def listOfNumber(listofnum):
    i=1
    list1=set()
    while True:
        if i>0:
            value=random.choice(new)
            list1.add(value)
        if len(list1)==num-1:
            break
        i=i+1
    return(list1)
numbers=new
num=listOfNumber(numbers)
secretNumlist=list(num)
print(secretNumlist) 
j=1
while j<=len(new):
    if j not in secretNumlist:
        print("Missing Num:-",j)
    j=j+1