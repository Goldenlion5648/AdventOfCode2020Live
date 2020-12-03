
'''
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
'''
from collections import *

with open("input3.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    board = f.read().strip().split("\n")

def slide(xChange, yChange):
    posX = 0
    posY = 0
    count = 0
    while posY < len(board):
        if board[posY][posX] == "#":
            count += 1
        posX = (posX + 3) % len(board[0])
        posY += 1
    return count

print("part 1", slide(3, 1))
#part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
nums = []
for x, y in slopes:
    nums.append(slide(x, y))

answer = 1
for i in nums:
    answer *= i
print("part 2", answer)