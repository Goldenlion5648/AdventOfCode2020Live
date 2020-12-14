
'''

'''
from collections import *

with open("input13.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")
time = int(a[0])
b = a[1].split(",")

c = []
for i in b:
    try:
        temp = int(i)
        c.append(temp)
        # print(i)
    except:
        pass
# print(c)
best = []
for i in c:
    cur = 1
    while i * cur < time:
        cur += 1
    else:
        best.append([i*cur - time, (i*cur - time) * i])

# print(best)
print("part 1", min(best)[1])

q = []
dis = []
for i in range(len(b)):
    if b[i] == "x":
        continue
    cur = int(b[i])
    dis.append([cur, cur-i])
# print(dis)

# not my code, taken from github, but I figured out chinese
# remainder theorem was what was going on in this problem
from functools import reduce
from typing import Tuple
num = 0
def chinese_remainder(n, a):
    sum2 = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum2 += a_i * mul_inv(p, n_i) * p
    return sum2 % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
 
# n = [3, 5, 7]
# a = [2, 3, 2]
a =[x[0] for x in dis]
b =[x[1] for x in dis]
# print(a)
# print(b)
print("part 2", chinese_remainder(a, b))



# answer = dis[0:2]
# temp = chinese_remainder_theorem(*dis[0:4])
# print(temp)
# # for i in range(2, len(dis), 2):
#     # answer = chinese_remainder_theorem(*answer, *dis[i:i+2])
# print(answer)
'''

'''
