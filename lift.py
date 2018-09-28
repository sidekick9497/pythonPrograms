up= 1
down = -1
Noclick = 0
clickStatus =[0,0,0,0,0,0,0,0]   
stopSequence = []
liftAt = 0
liftStatus = up
stop = False
# the required variables for the operation of lift are now set-up
clickStatus[2] = up
clickStatus[3] = down
clickStatus[5] = up
clickStatus[4] = down
clickStatus[7] = up
def callLift(direction,floor,clickStatus):
    clickStatus[floor] = direction
def hasElement(list,ele):
        flag = False
        for i in range(0,len(list)-1):
            if(list[i] == ele):
                flag = True
                break
        return flag   
def ExtremeFloor(clickStatus,direction):
    exFloor = 0
    if(direction == 1):
        # check the last 1 in the clickStatus
        for i in range(0,len(clickStatus)):
            if(clickStatus[i] == 1):
                exFloor = i

    else:
         for i in range(0,len(clickStatus)):
            if(clickStatus[i] == -1):
                exFloor = i
    return exFloor
def genItList(liftAt,exFloor):
      if(liftAt<exFloor):
            return range(liftAt,exFloor+1)
      else:
           return range(highFloor,exFloor-1,-1)

# setup all the required functions
#     
while(not stop):
   
    if(not (hasElement(clickStatus,1) or hasElement(clickStatus,-1))):
        stop = True
        break
    if(liftStatus == up):
        #do this
        # find the highest floor that lift has to go.. and stop at every floor in which the person needs to go up
        highFloor = ExtremeFloor(clickStatus,up)
        for i in genItList(liftAt,highFloor):
            #need to change stops to true in stop list
            if(clickStatus[i] == up):
                clickStatus[i] = 0
                stopSequence.append(i)
        liftAt = highFloor
        liftStatus = down        

    if(liftStatus == down):
        #do this  
        # find the lowest floor that lift has to go.. and stop at every floor in which the person need to go down  
        lowestFloor = ExtremeFloor(clickStatus,down)
        for i in genItList(liftAt,lowestFloor):
            #need to change stops to true in stop list
            if(clickStatus[i] == down):
                clickStatus[i] = 0
                stopSequence.append(i)
        liftStatus = up     

print(stopSequence)