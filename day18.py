
'''

'''
from collections import *
from math import *

with open("input18.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

# print(a)
answer = 0
probCount = 0
for i in a:
    pos = 0
    # cur = i.replace(" ", "")
    cur = i.replace("(", "[")
    cur = cur.replace(")", "]")
    cur = list(cur)
    parenCount = 0
    checkPoint = 0
    depth = 0
    hasChanged = False 
    points = [0]
    while pos < len(cur):
        if cur[pos].isnumeric():
            # print(cur[pos])
            # cur.insert(pos, "(")
            # if pos + 1 < len(cur) and cur[pos+1] != "]":
            cur.insert(pos+1, ")")
            cur.insert(checkPoint, "(")
            pos += 2
        if cur[pos] == "[":
            points.append(pos)
            # checkPoint = pos
            # depth += 1
        if cur[pos] == "]":
            # checkPoint = pos
            points.pop()
            checkPoint = points[-1]
            cur.insert(pos+1, ")")
            cur.insert(checkPoint, "(")
            pos += 2
            # depth -= 1
        # if depth == 0:
        #     checkPoint = 0

        checkPoint = points[-1]
        pos +=1
    # cur = list("(" * parenCount) + cur
    cur = "".join(cur)
    print(cur)
    cur = cur.replace("[", "(")
    cur = cur.replace("]", ")")
    # cur = cur.replace("()", "")
    print("".join(cur))
    tempSum = (eval(cur))
    print(tempSum)
    # print(i)
    # print(cur, "=", tempSum)
    answer += tempSum
    probCount += 1

print("probs", probCount)
print(answer)