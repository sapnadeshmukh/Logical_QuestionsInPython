number = [1,2,3,4,5,6,7,8,9]
i = 0
while i < len(number) - 1:
    var = number[i]
    number[i] = number[i + 1]
    number[i + 1] = var
    i = i + 2

print(number)