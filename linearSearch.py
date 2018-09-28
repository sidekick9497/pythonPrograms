myList = [1,3,4,5,6,7,8,21,23,45,67]
found = False
key = 200
position = 0
while found!=True and position<=len(myList)-1:
    if myList[position] == key: 
        found = True
    position +=1   
print found     