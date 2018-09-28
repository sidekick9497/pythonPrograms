myList = [1,3,4,5,6,7]
keys = [3,2,7,9]
def binSearch(searchList,keyList):
    foundCount = 0
    for key in keyList:
        found = False
        first = 0
        last = len(searchList)
        while found !=True and first <= last-1 :
            midpoint = (first + last)/2
            if searchList[midpoint] == key:
                print str(key) + " is in the list"
                foundCount+=1
                found = True
            else: 
                if first>= last:
                    break
                else:
                    if searchList[midpoint] > key:
                        last = midpoint-1
                    else:
                        first = midpoint+1 
        if not found:
            print str(key) + " is not in the list"
    hitRate = len(keyList)/foundCount
    print hitRate                        
binSearch(myList,keys)                        
