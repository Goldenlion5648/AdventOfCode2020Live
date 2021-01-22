from collections import *
from math import *
import random

with open("input20.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n\n")

print(a)
for i in range(len(a)):
    a[i] = a[i].split("\n")
print(a)
found = defaultdict(dict)
# found = dict()
pos = 0
other = 0
print(len(a))
# assert False
while other < len(a):
    # while other < len(a):
    cur = ""
    _, num = a[other][0].split(" ")
    # for i in range(len(a[1][1])):
    found[num][1] = list(a[other][1])
    found[num][2] = list("".join([a[other][i][0] for i in range(1, 11)]))
    found[num][3] = list(a[other][-1])
    found[num][4] = list("".join([a[other][i][-1] for i in range(1, 11)]))

    found[num][-1] = list(reversed(list(a[other][1])))
    found[num][-2] = list(reversed([a[other][i][0] for i in range(1, 11)]))
    found[num][-3] = list(reversed(list(a[other][-1])))
    found[num][-4] = list(reversed([a[other][i][-1] for i in range(1, 11)]))


    # for j in range(len(a[1][1])):
                # points[pos][i][j] = a[i][j]
    other += 1
    print(other)
    # pos += 1

# print(points)
print("found", found)
used = defaultdict(dict)
connections = defaultdict(dict)
# for z, ele in enumerate(found):
for z in found:
    for j in range(-4, 5):
        if j == 0:
            continue
        curSide = found[z][j]
        for x in found:
            if x == z:
                continue
            for i in range(-4, 5):
                if i == 0:
                    continue
                if curSide == found[x][i]:
                    used[z][j] = 1
                    used[x][i] = 1
                    used[z][-j] = 1
                    used[x][-i] = 1
                    print("added", used[z], z)
                    connections[z][i] = (x, j)
                    connections[x][j] = (z, i)
                    # connections[z][-j] = (x, -i)
                    # connections[x][i] = (z, j)
                    # connections[x][-i] = (z, -j)

print("used", used)
answer = []
# print("found", found)
for z in found:
    # for j in range(-4, 5):
        # if j == 0:
        #     continue
    if len(used[z]) == 4:
        answer.append(z)

answer.sort()
print(answer)
x = [int(i[:-1]) for i in answer]
print("part 1", prod(x))

print("connections", connections)
print(len(connections))
# assert False
boardDim = int(sqrt(len(connections)))
board = [[0 for i in range(boardDim)] for j in range(boardDim)]
orientations = board.copy()
orientations[0][0] = 3
# corners = []
print(answer)
for i in answer:
    print(i, connections[i])
board[0][0] = answer[-1]
allPieces = connections.keys()
# print(connections[board[0][0]].keys())
# curKeys = connections[board[0][0]].keys()
nextSide = abs(connections[board[0][0]].popitem()[0])
connections[board[0][0]].pop(-nextSide)
print(connections[board[0][0]])
print(nextSide)
for y in range(boardDim):
    for x in range(boardDim):
        print("x", x, "y", y)
        if x == 0:
            if y == 0:
                continue
            nextSide = abs(connections[board[y][x]].popitem()[0])
            
            continue
        if x != 0:
            prev = connections[board[y][x-1]]
            for j in prev:
                # board[y][x] = 
                pass
for i in board:
    print(i)
# for i in connections:
    # if len(connections[i]) == 4:
        # corners.append(i)
# print(corners)
# newImage = []
# fringe = answer[:]
# tileMap = dict()
# for i in range(len(a)):
#     cur = a[i][2:-1]
#     for j in range(len(cur)):
#         cur[j] = cur[j][1:-1]

#     tileMap[a[i][0].split(" ")[1]] = cur
# print("tilemap", tileMap)
# board = [[0 for i in range(len(found))] for j in range(len(found))]
# # print(board)
# posX = 0
# posY = 0
# board[0][0] = answer[0]
# topFaceNum = defaultdict(dict)
# nextTileNum = 0

# for i in answer:
#     print(i, ":", connections[i])

# board[0][0] = "1009:"
# sideNum = connections["1009:"][3][1]
# print("sideNum", sideNum)
# while posY < len(found):
#     while posX < len(found):
#         # for i in range(1, 5):
#         # if i==0:
#         #     continue
#         print("sideNum again:", sideNum)
#         print("cur connection",board[posY][posX], connections[board[posY][posX]])
#         tileID, sideNum = connections[board[posY][posX]][sideNum]
#         if posX + 1 < len(board):
#             board[posY][posX+1] = tileID
#             isNeg = False
#             if sideNum < 0:
#                 isNeg = True
#                 sideNum = abs(sideNum)
#             sideNum += 2
#             if sideNum > 4:
#                 sideNum = sideNum % 4
#             if isNeg:
#                 sideNum *= -1
#             # break

#         posX += 1
#         print("posX", posX)
#     posY += 1

# # for i in board:
#     # print(i)
# print(board[0])
# # while len(fringe):
# #     curTile = fringe.pop()
# #     inside = []
# #     print(tileMap[curTile])
# #     inside.append(tileMap[curTile][1:-1])
# #     inside[-1] = [i[1:-1] for i in inside[-1]]
# #     print(curTile)
# #     print(inside)
# #     newImage.append(inside[0])
# #     for i in range(2, 3):
# #         if i == 0:
# #             continue
# #         if i in connections[curTile]:
# #             fringe.append(connections[curTile][i])
# # for i in connections:

# # newVersion = []
# # for i in a:
# #     for j in range(2, len(i)-1):
# #         cur = i[j]
# #         newVersion.append(cur)

# # print(newVersion)


# '''

# '''
