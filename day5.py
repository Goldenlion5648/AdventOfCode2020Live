
'''

'''
from collections import *

with open("input5.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

highest = -1
seats = []
for i in a:
    # cur = "FBFBBFF"
    cur = i[0:7]
    cur = cur.replace("F", "0")
    cur = cur.replace("B", "1")
    # print(cur)
    cur = "0b" + cur
    end = i[7:]
    end = end.replace("R", "1")
    end = end.replace("L", "0")
    seats.append((int(cur, 2), int(end, 2)))
b = (max(seats, key = lambda x: x[0]))

print("part 1", b[0] * 8 + b[1])

seats.sort()
c = []
for i in seats:
    c.append((i[0] * 8 + i[1]))
    # print(i)
x = c[0]
for i in range(1, len(c)):
    if c[i] - 1 != x:
        print("part 2", c[i] - 1)
        break
    x = c[i]