from collections import *

with open("input9.txt") as f:
    a = list(map(int,f.read().strip().split("\n")))

b = deque()
for i in range(0, 25):
    for j in range(0, 25):
        b.append(a[i] + a[j])

pos = 25
while True:
    if a[pos] not in b:
        print("part 1:", a[pos])
        break
    for i in range(pos-25, pos):
        b.popleft()
        b.append(a[pos] + a[i])
    pos += 1

    
goal = 23278925
#part 2
stop = False
for i in range(len(a)):
    for j in range(i+1, len(a)):
        curSum = sum(a[i:j])
        if curSum == goal:
            c = min(a[i:j])
            d = max(a[i:j])
            print("part 2:", c + d)
            stop = True
        if curSum > goal:
            break
    if stop:
        break
