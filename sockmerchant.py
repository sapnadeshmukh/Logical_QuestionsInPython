def sockMerchant( list1):
    i=0
    count=0
    while i<len(list1):
        j=i+1
        while j<len(list1):
            if list1[i]==list1[j]:
                del(list1[i])
                count=count+1
                break
            j=j+1
        i=i+1
    print (count)
sockMerchant([1,2,1,2,1,3,2,1])