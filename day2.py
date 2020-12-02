
'''

'''
from collections import *

with open("input2.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

for x, ele in enumerate(a):
    a[x] = a[x].split()

# print(a)
count = 0

for x, ele in enumerate(a):
    print(ele)
    if int(ele[0].split("-")[0]) <= (ele[-1].count(ele[1][0])) <= int(ele[0].split("-")[1]):
        count += 1
print("part 1", count)

count = 0

for x, ele in enumerate(a):
    x = int(ele[0].split("-")[0])
    y = int(ele[0].split("-")[1])
    print(ele)
    if (x - 1 >= 0 and ele[-1][x-1] == ele[1][0]):
        if (y - 1 >= 0 and ele[-1][y-1] == ele[1][0]):
            pass
        else:
            count += 1
            print("added")
            continue
    if (y - 1 >= 0 and ele[-1][y-1] == ele[1][0]):
        if (x - 1 >= 0 and ele[-1][x-1] == ele[1][0]):
            pass
        else:
            count += 1
            print("added")
            continue
    
print("part 2", count)
