
'''

'''
from collections import *

with open("input14.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

print(a)
# for i in a:
mem = [0] * 100000
line = 0
cur = list('0' * 36)
print("cur", cur)

while True:

    if "mask" in a[line]:
        mask = a[line].split()[-1]
        line += 1
    while line < len(a) and "mem" in a[line]:
        # exec(a[line])
        b = a[line].split()
        num = int(b[-1])
        c = bin(num)[2:]
        c = "0" * (36 - len(c)) + c
        # print(c)
        # print("cur", "".join(cur))
        for x, ele in enumerate(cur):
            if mask[x] != "X":
                cur[x] = mask[x]
            else:
                cur[x] = c[x]
        # print(cur)
        # print(b[0][4:-1])
        mem[int(b[0][4:-1])] = int("".join(cur), 2)
        line += 1
    if line >= len(a):
        break 

print(mem)
print(sum(mem))


'''

'''
