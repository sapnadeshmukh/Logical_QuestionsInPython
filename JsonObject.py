json_object={"user":[{"username":"sapna","password":"sapna@21"},
                    {"username":"durga","password":"durga@21"},
                    {"username":"monik","password":"monik@21"}]}

value=json_object["user"]
user1=input("enter any name:--")
i=0
while i<len(value):
    if user1 in value[i]["username"]:
        print("already exists")
    else:
        print("Not exists")
    i=i+1
