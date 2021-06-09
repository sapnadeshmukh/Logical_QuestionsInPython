"""navgurukul is a good instituation."""
a=1
b=2
print(a+b)


def vowel_count(str):
    """This function count number of vowel in the string."""
    count=0
    for alphabet in str:
        if alphabet in "aeiouAEIOU":
            count=count+1
    return count
print(vowel_count.__doc__)

def name(str):
    """printing name"""
    nam=str+"deshmukh"
    return nam
print(name.__doc__)


def square(n):
    """Takes in a number n, returns the square of n"""
    return n**2
print(square(4))




# escape  sequence
print("he said,\"what's there?\" ")
print('''he said,"what's there?"''')



name="mysore palace?"
print(len(name))
print(name[2: 5])
print(name.upper())
print(name.capitalize())
print(name[-2])


k="All are small"
print(k.islower())


j="AASDFgm"
print(j.isupper())


string="iliketoeaticecream"
string="ABCDEFGH"

print(string[0:-1:34])

print("1.5".isnumeric())

string="fish"
print(string[0].capitalize() + string[1:-1] + string[-1].capitalize())
print(string[0].upper() + string[1:-1] + string[-1].upper())
print(string[0].replace("f","F") +string[1:-1] + string[-1].replace("h","H"))


# what does it mean for string to be immutable in python?
# ans:-- once a string object been created it can't be changeble("modify").that string create  whole new object in memory.


proverb="I am sapna"
print(id(proverb))
pro="SAPNa"
print(id(pro))
pro1="SAPNa"
print(id(pro1))



# concatinating:-variable create  object  with a new id .if object is actually modify then it would have the same id.



fullName=input("any input:--")
print(fullName)
newName=(fullName.split())
print(newName)
print(newName[0].capitalize() +newName[1].capitalize() + newName[2].upper())










   
   









