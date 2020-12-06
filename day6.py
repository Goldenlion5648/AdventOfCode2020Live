
'''

'''
from collections import *

with open("input6.txt") as f:
    # a = list(map(list,f.read().strip().split("\n")))
    a = f.read().rstrip().split("\n\n")
q = 0
for i in a:
    cur = i.split("\n")
    x = set(list(cur[0]))
    for j in range(len(cur)):
        x &= set(list(cur[j]))
    q += len(x)

for i in range(len(a)):
    a[i] = set(list(a[i]))
    a[i] = set([j for j in a[i] if j != '\n'])

total = 0
cur = a[0]
for i in a:
    total += len(i)
    cur ^= i

print("part 1", total)
print("part 2", q)
# print(cur)

'''

'''
