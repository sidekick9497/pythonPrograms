def generateSequence(n):
    number = 0
    current_digit = n
    multiplier = 1
    while(current_digit >= 1):
        number += (current_digit * multiplier)
        if(current_digit >= 10):
            multiplier *= 10
            if(current_digit >= 100):
                multiplier *= 10
        multiplier *= 10
        current_digit -= 1
    print(number)


n = int(input("Enter a number"))
for i in range(0, n + 1):
    generateSequence(i)
6
