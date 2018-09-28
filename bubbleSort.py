myList  = [7,3,4,1,8,9,2,6]
flag = True
while flag!=False:
    x = 0
    flag = False
    while x!= len(myList)-1:
        if myList[x] > myList[x+1]:
            myList[x],myList[x+1] = myList[x+1],myList[x]
            flag = True
        x +=1    
print myList
       