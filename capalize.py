def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
user=input("enter any string:--")
print(solve(user))