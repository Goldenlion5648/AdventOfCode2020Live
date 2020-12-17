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
        # for y in range(-1, 2):
        #     for x in range(-1, 2):
        #         if x == 0 and y == 0:
        #             continue
        #         if i + y >= 0 and i + y < len(board):
        #             if j + x >=0 and j + x < len(board[i]):
        #                 if board[i+y][j+x] == tileToLookFor:
        #                     count += 1
        for x in range(1, max(len(board), len(board[i]))):
            if i - x >= 0:
                cur = board[i -x][j]
                if cur != ".":
                    if cur == tileToLookFor:
                        count += 1
                    break
        for x in range(1, max(len(board), len(board[i]))):
            if i - x >= 0 and j - x >= 0:
                cur = board[i -x][j-x]
                if cur != ".":
                    if cur == tileToLookFor:
                        count += 1
                    break
        for x in range(1, max(len(board), len(board[i]))):
            if i - x >= 0 and j + x < len(board[0]):
                cur = board[i -x][j+x]
                if cur != ".":
                    if cur == tileToLookFor:
                        count += 1
                    break

        for x in range(1, max(len(board), len(board[i]))):
            if i + x < len(board):
                cur = board[i +x][j]
                if cur != ".":
                    if cur == tileToLookFor:
                        count += 1
                    break


        for x in range(1, max(len(board), len(board[i]))):
            if j - x >= 0:
                cur = board[i][j-x]
                if cur != ".":
                    if cur == tileToLookFor:
                        count += 1
                    break
        for x in range(1, max(len(board), len(board[i]))):
            if i + x < len(board) and j + x < len(board[0]):
                cur = board[i +x][j+x]
                if cur != ".":
                    if cur == tileToLookFor:
                        count += 1
                    break
        for x in range(1, max(len(board), len(board[i]))):
            if i + x < len(board) and j - x >= 0:
                cur = board[i +x][j-x]
                if cur != ".":
                    if cur == tileToLookFor:
                        count += 1
                    break

        for x in range(1, len(board[i])):
            if j + x < len(board[0]):
                cur = board[i][j+x]
                if cur != ".":
                    if cur == "L":
                        count += 1
                    break
            if tileToLookFor == "L":
                print("checked")
        
        # if count >= countNeeded:
        #     return True
        # return False


                        
        # print("count", count)
        if checkForMoreThan:
            if count >= countNeeded:
                return True
        else:
            if count == countNeeded:
                return True
       
 
           
    return False

def countAround2(i, j, tileToLookFor, board):
    count =0
    # print("checking", i, j)
    for x in range(1, max(len(board), len(board[i]))):
        if i - x >= 0:
            cur = board[i -x][j]
            if cur != ".":
                if cur == tileToLookFor:
                    count += 1
                    # print("was0")
                break
    for x in range(1, max(len(board), len(board[i]))):
        if i - x >= 0 and j - x >= 0:
            cur = board[i -x][j-x]
            if cur != ".":
                if cur == tileToLookFor:
                    count += 1
                    # print("was1")

                break
    for x in range(1, max(len(board), len(board[i]))):
        if i - x >= 0 and j + x < len(board[0]):
            cur = board[i -x][j+x]
            if cur != ".":
                if cur == tileToLookFor:
                    count += 1
                    # print("was9")

                break

    for x in range(1, max(len(board), len(board[i]))):
        if i + x < len(board):
            cur = board[i +x][j]
            if cur != ".":
                if cur == tileToLookFor:
                    count += 1
                    # print("was2")

                break


    for x in range(1, max(len(board), len(board[i]))):
        if j - x >= 0:
            cur = board[i][j-x]
            if cur != ".":
                if cur == tileToLookFor:
                    count += 1
                    # print("was3")
                
                break
    for x in range(1, max(len(board), len(board[i]))):
        if i + x < len(board) and j + x < len(board[0]):
            cur = board[i +x][j+x]
            if cur != ".":
                if cur == tileToLookFor:
                    count += 1
                    # print("was4")
                
                break
    for x in range(1, max(len(board), len(board[i]))):
        if i + x < len(board) and j - x >= 0:
            cur = board[i +x][j-x]
            if cur != ".":
                if cur == tileToLookFor:
                    count += 1
                    # print("was5")
                
                break

    for x in range(1, len(board[i])):
        if j + x < len(board[0]):
            cur = board[i][j+x]
            if cur != ".":
                if cur == tileToLookFor:
                    count += 1
                    # print("was6")

                break
    # print(i, j, count)
    return count


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
            
            # if temp[i][j] == "L":
            #     temp[i][j] = "#" if countAround2(i,j,"#", a) == 0 else "L"
            # if temp[i][j] == "#":
            #     temp[i][j] = "L" if countAround2(i,j,"#", a) >= 5 else "#"
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
    if a == temp:
        break
    for i in range(len(temp)):
        a[i] = temp[i].copy()
    # a = copy.deepcopy(temp)
    if a == prev:
        break
    for i in range(len(a)):
        prev[i] = a[i].copy()
    # prev = copy.deepcopy(a)
    for i in a:
        print("".join(i))
    print("="*48)

occ = 0
for i in a:
    occ += i.count("#")
    print("".join(i))

print(occ)




''' 

'''
