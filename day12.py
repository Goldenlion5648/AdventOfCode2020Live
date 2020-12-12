
'''

'''
from collections import *

with open("input12.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

x = 0
y = 0
angle = 90

wayX = 10
wayY = -1
for i in a:
    print(i)
    amount = int(i[1:])
    if i[0] =="W":
        wayX -= amount
    elif i[0] =="E":
        wayX += amount
    elif i[0] =="N":
        wayY -= amount
    elif i[0] =="S":
        wayY += amount

    if i[0] =="L":
            for q in range(amount//90):
                wayX, wayY = wayY, -wayX
                
        # if wayY > 0 and wayX > 0:
        #     wayX, wayY = -wayY, wayX
        # elif wayY > 0 and wayX < 0:
        #     wayX, wayY = -wayY, wayX
        # elif wayY < 0 and wayX < 0:
        #     wayX, wayY = wayY, -wayX
        # elif wayY < 0 and wayX > 0:
        #     wayX, wayY = -wayY, wayX

    if i[0] =="R":
            for q in range(amount//90):
                wayX, wayY = -wayY, wayX
        # if wayY > 0 and wayX > 0:
        #     wayX, wayY = wayY, -wayX
        # elif wayY > 0 and wayX < 0:
        #     wayX, wayY = wayY, -wayX
        # elif wayY < 0 and wayX < 0:
        #     wayX, wayY = wayY, -wayX
        # elif wayY < 0 and wayX > 0:
        #     wayX, wayY = wayY, -wayX

    if i[0] =="F":
        y += wayY * amount
        x += wayX * amount
    print(x, y,     wayX, wayY)

    # if i[0] =="L":
    #     angle -= amount
    # elif i[0] =="R":
    #     angle += amount
    # if i[0] =="F":
    #     if angle == 0:
    #         y -= amount
    #     elif angle == 180:
    #         y += amount
    #     if angle == 90:
    #         x += amount
    #     elif angle == 270:
    #         x -= amount

    angle = angle % 360

print(wayX, wayY)
print(abs(wayX) + abs(wayY))
print(x, y)
print(abs(x) + abs(y))
'''

'''
