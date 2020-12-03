
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
    # print(ele)
    l, r = list(map(int, ele[0].split("-")))
    if l <=  (ele[-1].count(ele[1][0])) <= r:
        count += 1
print("part 1", count)

count = 0

for x, ele in enumerate(a):
    x = int(ele[0].split("-")[0])-1
    y = int(ele[0].split("-")[1])-1
    # print(ele)
    if (ele[-1][x] == ele[1][0]) ^ (ele[-1][y] == ele[1][0] ):
        count += 1
    
print("part 2", count)





