def findCycleLength(number):
    counter = 1
    while (number != 1):
        if (number % 2 == 0):
            number /= 2
        else:
            number = (number*3)+1
        counter += 1
    return counter


def getMaxCycleLength(start, end):
    max_cycle_length = 0
    for number in range(start+1, end):
        cycle_length = findCycleLength(number)
        if (cycle_length > max_cycle_length):
            max_cycle_length = cycle_length
    print(max_cycle_length)


getMaxCycleLength(100, 200)
