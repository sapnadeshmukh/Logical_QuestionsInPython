listOfNumber=[[1,2,3],[4,5,6],[7,8,9]]
i=0
while i < len(listOfNumber):
    j=2
    while j<len(listOfNumber[i]):
        print(listOfNumber[i][j])
        j=j-1
        break
        
    i=i+1


