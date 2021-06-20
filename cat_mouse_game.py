cat1=int(input("enter a number"))
cat2=int(input("enter a number"))
mouse=int(input("enter a number"))



a=cat1-mouse
if (a>0):
    print(a)

else:
    a=(a)*-1
    print(a)

b=(cat2-mouse)
if(b>0):
    print(b)

else:
    b=(b*-1)
    print(b)


if(a>b):
    print("Cat2")

elif (a < b):
    print( "Cat1")

else:
    print("Mouse")
   


