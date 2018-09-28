# search using recursion and backTracking
list_items = [2,3,4,5,6,7,8,9]
def searchItem(listItems,key,index,backTrack):
    if index < 0:
        print("not found")
        return False
    if index < len(listItems)-1:
        if listItems[index] == key:
            print(" the key is found")
            return True
    if index >= len(listItems)-1:
        backTrack = True
        if backTrack:
            if len(listItems) % 2 == 0:
                index -=1
            else:
                index -= 2 
            return searchItem(listItems,key,index,backTrack)
    if backTrack:
        return searchItem(listItems,key,index-1,backTrack)   
    return searchItem(listItems,key,index+2,backTrack)
searchItem(list_items,12,1,False)        
