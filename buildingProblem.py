def getAmount(number_of_streets):
    amountList = [0]*(number_of_streets)
    for i in range(0, number_of_streets):
        amountList[i] = int(input("enter the amount for the street"))
    return amountList


def getHeights(number_of_streets):
    heights_of_builidings = []
    for i in range(0, number_of_streets):
        number_of_buildings = int(input("enter the number of builidings : "))
        buildingList = []
        for j in range(0, number_of_buildings):
            height = int(input("enter the heights of buildings :"))
            buildingList.append(height)
        heights_of_builidings.append(buildingList)
    return heights_of_builidings


def calculate(heightsList, cost):
    street_salary = 0
    max_height_index = 0
    street_salary += cost
    for i in range(1, len(heightsList)):
        if (heightsList[i] > heightsList[max_height_index]):
            max_height_index = i
            street_salary += cost

    return street_salary


def getSalary(number_of_streets):
    amount_for_each_street = getAmount(number_of_streets)
    heights_of_builidings = getHeights(number_of_streets)
    salary = 0
    print(amount_for_each_street)
    print(heights_of_builidings)
    for i in range(0, number_of_streets):
        salary += calculate(heights_of_builidings[i],
                            amount_for_each_street[i])
    print(salary)
    
getSalary(2)
