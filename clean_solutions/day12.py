from collections import *

with open("input12.txt") as f:
    a = f.read().strip().split("\n")

def part1(a):
    x = 0
    y = 0
    angle = 90
    for i in a:
        amount = int(i[1:])
        if i[0] =="W":
            x -= amount
        elif i[0] =="E":
            x += amount
        elif i[0] =="N":
            y -= amount
        elif i[0] =="S":
            y += amount
        angle = angle % 360

        if i[0] =="L":
            angle -= amount
        elif i[0] =="R":
            angle += amount
        if i[0] =="F":
            if angle == 0:
                y -= amount
            elif angle == 180:
                y += amount
            if angle == 90:
                x += amount
            elif angle == 270:
                x -= amount
    print("part 1:", abs(x) + abs(y))

def part2(a):
    x = 0
    y = 0
    angle = 90
    wayX = 10
    wayY = -1
    for i in a:
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
        if i[0] =="R":
            for q in range(amount//90):
                wayX, wayY = -wayY, wayX

        if i[0] =="F":
            y += wayY * amount
            x += wayX * amount

    
    print("part 2:", abs(x) + abs(y))
part1(a)
part2(a)
