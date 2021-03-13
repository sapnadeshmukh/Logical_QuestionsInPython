a=["sapna","durga","abhi","papa","somi"]
i=0
user=input("enter string")

while (i <len(a)):
    if user in a[i][0]:
        print(a[i])
    i=i+1
