
'''

'''
from collections import *

with open("input3.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")
board = list(map(list, a))
print(board)
posX = 0
posY = 0
nums = []
count = 0
while posY < len(board):
    if board[posY][posX] == "#":
        count += 1
    posX = (posX + 3) % len(board[0])
    posY += 1
print("part 1", count)
nums.append(count)
posX = 0
posY = 0
count = 0
while posY < len(board):
    if board[posY][posX] == "#":
        count += 1
    posX = (posX + 1) % len(board[0])
    posY += 1
nums.append(count)
posX = 0
posY = 0
count = 0
while posY < len(board):
    if board[posY][posX] == "#":
        count += 1
    posX = (posX +5) % len(board[0])
    posY += 1
nums.append(count)
posX = 0
posY = 0
count = 0
while posY < len(board):
    if board[posY][posX] == "#":
        count += 1
    posX = (posX + 7) % len(board[0])
    posY += 1
nums.append(count)
posX = 0
posY = 0
count = 0
while posY < len(board):
    if board[posY][posX] == "#":
        count += 1
    posX = (posX + 1) % len(board[0])
    posY += 2
nums.append(count)
answer = 1
for i in nums:
    answer *= i
print("part 2", answer)