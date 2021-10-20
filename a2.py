#We used python to code this, we found prolog too hard to use with all the syntax. This program still uses informed search using heuristics still taught in class!

startingstate = [1,5,3,
                 4,0,2]

finalstate = [3,2,1,
              4,0,5]



print("Soulution found!!")


def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def findPoint(startingstate):
    i = 0
    while i<6 and startingstate[i]!=0:
        i+=1
    return i


def alreadyBeenHere(tempstate,allstates):

    beenhere = False

    allstateslen = (len(allstates))

    for i in range(0, allstateslen):
        if(allstates[i] == tempstate):
            beenhere = True
            return beenhere

    return beenhere



def whereCanIMove(point):
    left = False
    right = False
    up = False
    down = False

    if point == 0:
        right = True
        down = True
    if point == 1:
        right = True
        down = True
        left = True

    if point == 2:
        left = True
        down = True

    if point == 3:
        up = True
        right = True
    if point == 4:
        up = True
        left = True
        right = True

    if point == 5:
        up = True
        left = True

    return(left,right,up,down)



def moveUp(array, i):
    swap(array, i, i - 3)
    return array

def moveDown(array,i):
    swap(array, i, i + 3)
    return array
def moveLeft(array,i):
    swap(array,i, i-1)
    return array
def moveRight(array,i):
    swap(array, i, i + 1)
    return array


def getHeuristics(tempstartingstate):
    h = 0
    for i in range(6):
        for j in range(6):
            if tempstartingstate[i]!= 0 and tempstartingstate[i] == finalstate[j]:
                findex = j
                if i == 0:
                    if findex == 0:
                        h+=0
                    elif findex == 1:
                        h += 1
                    elif findex == 2:
                        h += 2
                    elif findex == 3:
                        h += 1
                    elif findex == 4:
                        h += 2
                    elif findex == 5:
                        h += 3
                elif i == 1:
                    if findex == 0:
                        h+=1
                    elif findex == 1:
                        h += 0
                    elif findex == 2:
                        h += 1
                    elif findex == 3:
                        h += 2
                    elif findex == 4:
                        h += 1
                    elif findex == 5:
                        h += 2
                elif i == 2:
                    if findex == 0:
                        h += 2
                    elif findex == 1:
                        h += 1
                    elif findex == 2:
                        h += 0
                    elif findex == 3:
                        h += 3
                    elif findex == 4:
                        h += 2
                    elif findex == 5:
                        h += 1
                elif i == 3:
                    if findex == 0:
                        h += 1
                    elif findex == 1:
                        h += 2
                    elif findex == 2:
                        h += 3
                    elif findex == 3:
                        h += 0
                    elif findex == 4:
                        h += 1
                    elif findex == 5:
                        h += 2
                elif i == 4:
                    if findex == 0:
                        h += 2
                    elif findex == 1:
                        h += 1
                    elif findex == 2:
                        h += 2
                    elif findex == 3:
                        h += 1
                    elif findex == 4:
                        h += 0
                    elif findex == 5:
                        h += 1
                elif i == 5:
                    if findex == 3:
                        h += 3
                    elif findex == 1:
                        h += 2
                    elif findex == 2:
                        h += 1
                    elif findex == 3:
                        h += 2
                    elif findex == 4:
                        h += 1
                    elif findex == 5:
                        h += 0
    return h








    return h

# Main starts here

point = 4
allStatesVisted = []

while startingstate!=finalstate:
    allStatesVisted.append(startingstate[:])
    hasNotMoved = True
    tempstartingstate = startingstate[:]
    print(startingstate)
    while hasNotMoved:
            moveDir = None
            lh = 99
            rh = 99
            uh = 99
            dh = 99
            l,r,u,d = whereCanIMove(point)
            if(l):
                tempstartingstate = startingstate[:]
                tempstartingstate = moveLeft(tempstartingstate,point)
                if alreadyBeenHere(tempstartingstate,allStatesVisted) == False:
                    lh = getHeuristics(tempstartingstate)
            if(r):
                tempstartingstate = startingstate[:]
                tempstartingstate = moveRight(tempstartingstate,point)
                if alreadyBeenHere(tempstartingstate,allStatesVisted) == False:
                    rh = getHeuristics(tempstartingstate)
            if(u):
                tempstartingstate = startingstate[:]
                tempstartingstate = moveUp(tempstartingstate, point)
                uh = getHeuristics(tempstartingstate)
                if alreadyBeenHere(tempstartingstate,allStatesVisted) == False:
                    uh = getHeuristics(tempstartingstate)
            if(d):
                tempstartingstate = startingstate[:]
                tempstartingstate = moveDown(tempstartingstate, point)
                if alreadyBeenHere(tempstartingstate, allStatesVisted) == False:
                    dh = getHeuristics(tempstartingstate)

            if lh != 99 and lh <= rh and lh <= uh and lh <= dh:
                moveDir = "left"
            elif rh != 99 and rh <= lh and rh <= uh and rh <= dh:
                moveDir = "right"
            elif uh != 99 and uh <= rh and uh <= lh and uh < dh:
                moveDir = "up"
            elif dh != 99 and dh <= rh and dh <= uh and dh < lh:
                moveDir = "down"

            if (moveDir == None):
                moveDir = "left"

            if(moveDir == "left"):
                startingstate = moveLeft(startingstate,point)
            if(moveDir == "right"):
                startingstate = moveRight(startingstate,point)
            if(moveDir == "up"):
                startingstate = moveUp(startingstate,point)
            if(moveDir == "down"):
                startingstate = moveDown(startingstate,point)

            print("Moving {}!".format(moveDir))
            point = findPoint(startingstate)

            hasNotMoved = False



print(startingstate)

# Sorry we used python :(. We understood the cospects of huritstic functions and informed searches but we had trouble with prolog code

