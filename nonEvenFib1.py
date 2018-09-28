#use binets formula to generate fibonacci number
def binetsFib(n):
    phi = (1 + 5**0.5)/2.0
    return int(round((phi**n-(1-phi)**n)/5**0.5))    
# generate fibonacci series
def generateFib(limit):
    fibSequence = []
    for i in range(1, limit+1):
        fibSequence.append(binetsFib(i))
    return fibSequence    
# use fibonacci series to generate nonFibonacci number series
def nonFib(fibonacciList,limit):
    nonFibSequence = []
    i=0
    while i != limit:
        low = fibonacciList[i]
        high = fibonacciList[i+1]
        while low != high:
            if high-low != 1:
                nonFibSequence.append(low+1)
            low+=1
        i+=1    
    return nonFibSequence
# grab the nonFibonacci Numbers from the given list    
def getNonFib(indexList):
    resultList = []
    #just to make sure that we generate enough nonFibonacci numbers
    nonFiblist = nonFib(generateFib(max(indexList)+5),max(indexList)+4) 
    for i in indexList:
        resultList.append(nonFiblist[i-1])
       
    return resultList
indices = [3,1,2,3]
print getNonFib(indices)    
    