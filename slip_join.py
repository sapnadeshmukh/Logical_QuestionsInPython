def split_and_join(line):
    a = line.split(" ")
    result = "-".join(a)
    return result


line = input("enter any string:-")
result = split_and_join(line)
print(result)