def ExtremeFloor(clickStatus,direction):
    exFloor = 0
    if(direction == 1):
        # check the last 1 in the clickStatus
        for i in range(0,len(clickStatus)):
            if(clickStatus[i] == 1):
                exFloor = i

    else:
         for i in range(len(clickStatus)-1,0,-1):
            if(clickStatus[i] == -1):
                exFloor = i
    return exFloor
list = [1,-1,1,1,-1,1,-1,1,0,0]
print(ExtremeFloor(list,1))
print(ExtremeFloor(list,-1))