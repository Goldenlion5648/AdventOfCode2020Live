from collections import *
from math import *

with open("input24.txt") as f:
    a = f.read().strip().split("\n")
allPositions = dict()
for i in range(-100, 100):
    for j in range(-200, 200):
        allPositions[(i, j/2)] = 0

flipped = set()
for line in a:
    i = 0
    # print(line)
    posX = 0
    posY = 0
    while i < len(line):
        if line[i] == "s":
            posY -= 1
            if line[i+1] == "e":
                posX += .5
                i += 1
            else:
                posX -= .5
                i += 1
        elif line[i] == "n":
            posY += 1
            if line[i+1] == "e":
                posX += .5
                i += 1
            else:
                posX -= .5
                i += 1
        elif line[i] == "e":
            posX += 1
        elif line[i] == "w":
            posX -= 1
        i += 1
    cur = (posY, float(posX))
    # print(cur)
    if cur in flipped:
        # print("removing")
        flipped.remove(cur)
    else:
        flipped.add(cur)
print("part 1:", len(flipped))

for i in flipped:
    allPositions[i] = 1


def checkAround(a, flipped):
    posY, posX = a
    neigh = 0
    if (posY, posX-1) in flipped and flipped[(posY, posX-1)] == 1:
        neigh += 1
    if (posY, posX+1) in flipped and flipped[(posY, posX+1)] == 1:
        neigh += 1
    if (posY-1, posX+.5) in flipped and flipped[(posY-1, posX+.5)] == 1:
        neigh += 1
    if (posY+1, posX+.5) in flipped and flipped[(posY+1, posX+.5)] == 1:
        neigh += 1
    if (posY-1, posX-.5) in flipped and flipped[(posY-1, posX-.5)] == 1:
        neigh += 1
    if (posY+1, posX-.5) in flipped and flipped[(posY+1, posX-.5)] == 1:
        neigh += 1
    return neigh

def addToFringe(curBlack, allPositions):
    fringe = dict()
    for point in curBlack:
        fringe.update(addAroundPoint(point, allPositions))
    return fringe

def addAroundPoint(point, allPositions):
    fringe = dict()
    posY, posX = point
    fringe[(point)] = allPositions[(point)]
    fringe[((posY, posX-1))] = allPositions[((posY, posX-1))]
    fringe[((posY, posX+1))] = allPositions[((posY, posX+1))]
    fringe[((posY-1, posX+.5))] = allPositions[((posY-1, posX+.5))]
    fringe[((posY+1, posX+.5))] = allPositions[((posY+1, posX+.5))]
    fringe[((posY-1, posX-.5))] = allPositions[((posY-1, posX-.5))]
    fringe[((posY+1, posX-.5))] = allPositions[((posY+1, posX-.5))]
    return fringe
# newFlip = list(flipped)
tempFringe = addToFringe(flipped, allPositions)
# tempFringe = addToFringe
for day in range(1, 101):
    j = 0
    pointsToChange = dict()
    # fringe = addToFringe(tempFringe, allPositions)
    # fringe = addToFringe(fringe)
    # tempFringe = dict()
    for point in allPositions:
        count =checkAround(point, allPositions) 
        if allPositions[point] == 1 and (count == 0 or count > 2):
            pointsToChange[point] = 0
        elif allPositions[point] == 0 and count == 2:
            pointsToChange[point] = 1
        # if count > 0:
    # tempFringe.update(addAroundPoint(point, allPositions))
    for i in pointsToChange:
    # allPositions.difference_update(pointsToChange)
        allPositions[i] = pointsToChange[i]
    print("day", day)
    # print("len of fringe", len(fringe))
    if day % 10 == 0:
        print(sum(allPositions.values()))

              
print("part 2", sum(allPositions.values()))
