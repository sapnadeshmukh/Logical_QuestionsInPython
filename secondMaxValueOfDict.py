dic={1:2,2:3,4:5,7:6}
max=max(dic.values())
max2=0
for x in (dic.values()):
    if x>max2 and x<max:
        max2=x
print(max2)