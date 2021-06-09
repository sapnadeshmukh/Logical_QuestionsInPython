output = [] 
def reemovNestings(listNum):
    for index in listNum:
        if type(index) == list:
            reemovNestings(index)
        else:
            output.append(index)
  
l=[1,2,3,[4,[5,6,[7,12,21]],8],[9]] 

print(l)
reemovNestings(l)
print (output)


