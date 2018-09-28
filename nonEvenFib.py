def binetsFib(n):
    phi = (1 + 5**0.5)/2.0
    return int(round((phi**n-(1-phi)**n)/5**0.5))

def getNonFib(pos):
     init = 1
     count = 0
     fib = 0
     while(count <= pos):
         fib = binetsFib(init)
         if(init != fib):
            count+=1
         init+=1
     return init 
print(getNonFib(5))
