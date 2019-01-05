#step generate the primes for that number
#step2 do the factorization of the number
#step3 make the set of the factorization
#check for the special number  condition
def specialNumber(number,specialNumber_length):
    primes = generatePrimes(number)
    factors = generateFactors(number,primes)
    set_of_factors = list(set(factors))
    length = len(set_of_factors)
    if(length == specialNumber_length):
        print("yes")
    else:
        print("No")

def generatePrimes(number):
    primes = []
    primes.append(2)
    for i in range(3,number+1,2):
        flag = True
        for j in range(3,i):
            if(i%j == 0):
                flag = False
        if(flag):
            primes.append(i)
    return primes
def generateFactors(number,primes):
    factors = []
    counter = 0
    while(number >1):
        current_divider = primes[counter]
        if(number % current_divider == 0):
            number = number /current_divider
            factors.append(current_divider)
        else:
            counter +=1
    return factors
print(specialNumber(30,3))



                