# if user give nth number then nth number should print from last of list
marks=["1","2","3","5","b","q"]
user=int(input("enter num"))
l=len(marks)-1
i=0
while i<user:
    print(marks[l])
    l=l-1
    i=i+1
    

