item_list = [{'item': 'item1', 'amount': 400}, 
            {'item': 'item2', 'amount': 300}, 
            {'item': 'item1', 'amount': 250},
            {'item':'item1','amount':200},
            {'item': 'item2', 'amount': 300}]
# o/p=Counter({'item1': 1150, 'item2': 300})
i=0

main={}
sum=0
sum2=0
for i in item_list:
    if "item1" in i["item"]:
        sum=sum+i["amount"]
        main["item1"]=sum
    else:
        sum2=sum2+i["amount"]
        main["item2"]=sum2
print(main)


        
