import copy
'''
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
'''
from collections import *

def checkAround(i, j, board, tileToLookFor, changeTo, countNeeded, cur, isNot, checkForMoreThan):
    # print("Checking", i, j)
    count = 0
    if board[i][j] == cur:
        for y in range(-1, 2):
            for x in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                if i + y >= 0 and i + y < len(board):
                    if j + x >=0 and j + x < len(board[i]):
                        if board[i+y][j+x] == tileToLookFor:
                            count += 1
                        
        # print("count", count)
        if checkForMoreThan:
            if count >= countNeeded:
                # board[i][j] = changeTo
                # print("changed1", i,j)
                return True
        else:
            if count == countNeeded:
                # board[i][j] = changeTo
                # print("changed1", i,j)
                return True
       
        # else:
        #     if count >= countNeeded:
        #         board[i][j] = changeTo
        #         # print("changed1", i,j)
        #         return True
           
    return False
    # print("count was", count)
    # return board

with open("input11.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

a = list(map(list, a))
# print(a)
temp = copy.deepcopy(a)
for i in a:
    print("".join(i))
print("="*48)
prev = a.copy()
for x in range(1000):
    for i in range(len(a)):
        for j in range(len(a[i])):
            

            temp[i][j] = "#" if copy.deepcopy(\
                checkAround(i, j, a, "#",
             "#", 0, "L", False, False)) else temp[i][j] 

            temp[i][j] = "L" if copy.deepcopy(\
                checkAround(i, j, a, "#",
             "L", 5, "#", False, True)) else temp[i][j] 
        # for i in a:
        #     print("".join(i))
        # print("9"*48)
    # a = []
    for i in range(len(temp)):
        a[i] = temp[i].copy()
    # a = copy.deepcopy(temp)
    if a == prev:
        break
    for i in range(len(a)):
        prev[i] = a[i].copy()
    # prev = copy.deepcopy(a)
    # for i in a:
    #     print("".join(i))
    print("="*48)

occ = 0
for i in a:
    occ += i.count("#")
    print("".join(i))

print(occ)




''' 

'''
