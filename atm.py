def language():
    if user==1:
        a= "English"
    else:
        a= "Hindi"
    return user
user=int(input("Choose your Langugae \n 1.English \n 2.Hindi="))
# choose=language()
def pin_code(choose):
    if choose==1:
        i=0
        while i<3:
            pin=int(input("enter your four digit pin number="))
            if pin== 1234:
                b="correct"
                break
            else:
                b="inncorect Pin!"
            i+=1
        return b
    else:
        i=0
        while i<3:
            pin=int(input("Apna char number ka pin Darj kare="))
            if pin== 1234:
                a=("Aapka pin sahi hai")
                break
            else:
                a=("Fir se apna pin dale")
            i+=1
        return a      
code=pin_code(user)
# print(code)
def options(choose):
    if choose==1:
        balance=35000
        print('please press 1 for your balance inquiry')
        print('please press 2 for your withdrawl')
        print('please press 3 for your pay in')
        print('please press 4 for your return card/ Exit')
        print(".............")
        option=int(input('what would you like to choose='))
        if option ==1:
            ans= balance,"Your current balance"
        elif option ==2:
            withdrwal=int(input("enter how much money would you like to withdrawl="))
            ans=balance-withdrwal,"Your Current balance"
        elif option ==3:
            pay=int(input("enter how much money you want to pay in="))
            ans= balance + pay,"you current balance"
        else:
            ans= "collect your card"
            print("THANK YOU FOR VISIT")
    
    else:
        balance=20000
        print('Kripya karke 1 dbaye apni Jma rashi ke bare me janne ke liye')
        print('Pese nikalne ke liye 2 Dbaye')
        print('Pese Jma karne ke liye 3 dbaye')
        print('Apna card wapis lene ke liye 4 dbaye')
        print("...........")
        option=int(input("kripya karke apna Vikalp chune="))
        if option ==1:
            ans= balance,"Apki kul jma rashi"
        elif option ==2:
            withdrwal=int(input("Aap kitni rashi nikalna chahoge?="))
            ans=balance-withdrwal,"apki kil jma rashi"
        elif option ==3:
            pay=int(input("Aap kitna Bhugtan karna chahoge?="))
            ans= balance + pay,"Apki Kul Jma rashi"
        else:
            ans= "Apna card Jma kar lijiye"
            print("Dhanyawad Aane Ke liye")
    return ans
option=options(user)
print(option)