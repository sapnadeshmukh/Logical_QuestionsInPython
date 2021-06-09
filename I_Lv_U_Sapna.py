# fro heart
import math

c='♥'


width = 40

print ((c*2).center(width//2)*2)

for i in range(1,width//10+1):
    print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
           (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

for i in range(width//4,0,-1):
    print ((c*i*4).center(width))
print ((c*2).center(width))






# for I
# take 5 as input
def print_pattern(n):
    # Outer for loop for number of rows
    for rows in range(n):
 
        # Inner for loop columns
        for columns in range(n):
 
            # prints first and last row
            if ((rows == 0 or rows == n-1) or
               # prints middle column
                (columns == n // 2)
            ):
                print("♥", end=" ")
            else:
                print(" ", end=" ")
        print()
 
 
size = int(input("Enter size:--"))
print_pattern(size)
print( )
print(    )


# for small heart
for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("♥",end="")
        else:
            print(end=" ")
    print( )


print( )

# for U
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4 ) and row!=6) or (row==6 and (col>0 and col<4)):
            print("♥",end="")
        else:
            print(end=" ")
    print()

print( )

# for S
for row in range(7) :
    for col in range(5):
        if ((row==0 or row==3 or row==6 )  and (col>0 and col<4)) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
            print('♥',end="" )
        else:
            print(end=" ")
    print()


print( )  



# for A
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4)and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("♥",end="")
        else:
            print(end=" ")
    print()

print( )

# for P
for row in range(7):
    for col in range(5):
        if col==0 or (col==4 and (row==1 or row==2)) or ((row==0 or row==3) and (col>0 and col<4)):
            print("♥",end=" ")
        else:
            print(end="  ")
    print()
print( )

# for N
for row in range(6):
    for col in range(6):
        if col==0 or col==5 or (row==col and (col>0 and col<5)):
            print("♥",end="")
        else:
            print(end=" ")
    print()

print( )
# for A
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4)and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("♥",end="")
        else:
            print(end=" ")
    print()

print( )









