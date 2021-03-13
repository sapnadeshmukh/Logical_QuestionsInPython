string="I am sapna D"
upper = 0
lower = 0
i=0
while i <len(string): 
          
    # For lower letters 
    if (ord(string[i]) >= 97 and
        ord(string[i]) <= 122): 
        lower = lower+1

    # For upper letters 
    elif (ord(string[i]) >= 65 and
            ord(string[i]) <= 90): 
        upper =upper+1 
    i=i+1
print("Lower case characters =",lower , 
      "Upper case characters = ",upper) 
  