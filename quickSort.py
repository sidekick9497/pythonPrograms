def quickSort(myList,start,end):
    if start < end:
        pivot = partition(myList,start,end)
        quickSort(myList,start,pivot-1)
        quickSort(myList,pivot+1,end)
    return myList    

def partition(myList,start,end):
    pivot = myList[start]
    left = start + 1
    right = end
    completed = False
    while not completed:
        while left <= right and myList[left]<=pivot:
            left +=1
        while myList[right]>=pivot and right >= left:
            right -= 1 
        if right <= left:
            completed = True
        else:
            myList[left],myList[right] = myList[right],myList[left]
    myList[start],myList[right] = myList[right],myList[start]
    return right

thisList   = [3,2,6,7,1,8]
quickSort(thisList,0,len(thisList)-1)   
print thisList                