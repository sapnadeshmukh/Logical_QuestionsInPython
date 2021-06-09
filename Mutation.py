

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

    
    

s = input("enter any string:-")
i, c = input("enter postion and new leter:---").split()
s_new = mutate_string(s, int(i), c)
print(s_new)