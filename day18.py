
'''

'''
from collections import *
from math import *

with open("input18.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

# print(a)
def part1():
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
        # print(cur)
        cur = cur.replace("[", "(")
        cur = cur.replace("]", ")")
        # cur = cur.replace("()", "")
        # print("".join(cur))
        tempSum = (eval(cur))
        # print(tempSum)
        # print(i)
        # print(cur, "=", tempSum)
        answer += tempSum
        probCount += 1
    return answer

def part2():
    answer = 0
    count = 0
    for i in a:
        # print("problem number", count)
        # print(i)
        count += 1
        cur = i.replace("(", "[")
        cur = cur.replace(")", "]")
        cur = list(cur)
        pos = 0
        while pos < len(cur):
            # print("cur", "".join(cur))
            if cur[pos] == "+":
                temp = pos
                depth = 0
                while True:
                    # if temp == len(cur) or \
                    # (cur[temp] == "*" and depth == 0) :
                    if temp == len(cur):
                        cur.insert(temp, ")")
                        break
                    elif cur[temp] == "*" and depth == 0:
                        cur.insert(temp-1, ")")
                        break
                    elif cur[temp] in "])" and depth == 0:
                        cur.insert(temp, ")")
                        break
                    # temp

                    if cur[temp] in "([":
                        depth += 1
                    if cur[temp] in ")]":
                        depth -= 1

                    temp += 1
                    # print(temp)
                # endPos = temp
                if cur[pos-2].isnumeric(): 
                    cur.insert(pos- 2, "(")
                else:
                    temp = pos-2
                    depth = 0
                    while True:
                        # print("temp", temp)
                        if temp == 0:
                            cur.insert(temp, "(")
                            break
                        if cur[temp] in "([":
                            depth += 1
                        if cur[temp] in ")]":
                            depth -= 1
                        if (depth == 0):
                            cur.insert(temp, "(")
                            break
                        temp -= 1
                # pos = endPos

                pos += 1


            pos += 1
        cur = "".join(cur)
        cur = cur.replace("[", "(((((")
        cur = cur.replace("]", ")))))")
        # cur = cur.replace("()", "")

        # print(cur)
        curAnswer = eval(cur)
        # print(cur, "=", curAnswer)
        answer += curAnswer
    return answer
# print("probs", probCount)
print("part1", part1())
print("part2", part2())