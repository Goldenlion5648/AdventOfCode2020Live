from collections import *
from math import *

with open("input24.txt") as f:
    a = f.read().strip().split("\n")
allPositions = []
for i in range(-100, 100):
    for j in range(-200, 200):
        allPositions.append((i, j/2))

flipped = set()
for line in a:
    i = 0
    print(line)
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

def checkAround(a, flipped):
    posY, posX = a
    neigh = 0
    if (posY, posX-1) in flipped:
        neigh += 1
    if (posY, posX+1) in flipped:
        neigh += 1
    if (posY-1, posX+.5) in flipped:
        neigh += 1
    if (posY+1, posX+.5) in flipped:
        neigh += 1
    if (posY-1, posX-.5) in flipped:
        neigh += 1
    if (posY+1, posX-.5) in flipped:
        neigh += 1
    return neigh

newFlip = list(flipped)

for day in range(1, 101):
    j = 0
    print("day", day)
    tempFlipped = newFlip.copy()
    while j < len(newFlip):
        # print("cur", newFlip[j])
        count =checkAround(newFlip[j], newFlip) 
        if count == 0 or count > 2:
            tempFlipped.remove(newFlip[j])
        j += 1
    for x, ele in enumerate(allPositions):
        if ele not in newFlip and checkAround(ele, newFlip) == 2:
            tempFlipped.append(ele)
    newFlip = tempFlipped.copy()

              
    print(len(newFlip))
# print(len(flipped))