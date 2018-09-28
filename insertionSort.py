myList  = [7,3,4,1,8,9,2,6]  
i = 1
while i<len(myList):
    j = i
    while j>0 and myList[j-1]>myList[j]:
        myList[j-1],myList[j] = myList[j],myList[j-1]
        j -= 1
    i +=1
print myList        