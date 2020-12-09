
'''

'''
from collections import *

with open("input9.txt") as f:
    a = list(map(int,f.read().strip().split("\n")))


b = deque()
for i in range(0, 25):
    for j in range(0, 25):
        # if i == j:
            # continue
        b.append(a[i] + a[j])

print(b)
print(len(b))
pos = 25
while True:
    if a[pos] not in b:
        print(a[pos])
        break
    for i in range(pos-25, pos):
        b.popleft()
        b.append(a[pos] + a[i])
    pos += 1
        # break
goal = 23278925

stop = False
for i in range(len(a)):
    for j in range(i+1, len(a)):
        curSum = sum(a[i:j])
        if curSum == goal:
            c = min(a[i:j])
            d = max(a[i:j])
            print(c + d)
            stop = True
        if curSum > goal:
            break
    if stop:
        break
# left = 0
# right = 1
# curSum =sum(a[left:right])
# while curSum != goal:
#     if curSum < goal:
#         right += 1


'''

'''
