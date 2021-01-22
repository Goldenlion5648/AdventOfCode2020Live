
'''

'''
from collections import *
from math import *

with open("input23.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    # a = f.read().strip().split("\n")
    a = f.read().strip()

a = list(a)
a = list(map(int,a))
a = deque(a)
print(a)
pos = 0
cur = a[pos]
for j in range(100):
    temp = a.copy()
    cur = a[pos]
    selected = []
    while temp[0] != cur:
        temp.rotate(-1)
    temp.rotate(-1)
    print("temp before", temp)
    for i in range(3):
        # selected.append(temp.pop((pos + 1)%len(a)))
        selected.append(temp.popleft())

    temp.rotate(1)
    print("temp after", temp)
    print("pick up", selected)
    # cur = a.index(cur - 1)
    dest = cur - 1
    print("dest", dest)
    while dest in selected:
        dest = dest - 1
        if dest <= 0:
            dest = 9
    print("after dest", dest)
    # d = a.index(dest)
    new = [] 
    while len(temp) > 0 and temp[0] != dest:
        new.append(temp.popleft())
    new.append(temp.popleft())
    new += selected
    new += list(temp)
    # temp.rotate(-3)
    # while len(temp) > 0 and temp[0] != dest:
    #     new.append(temp.popleft())
    # else:
    #     new += selected
    # while len(temp):
    #     new.append(temp.popleft())
    pos += 1
    pos %= 9
    a = deque(new)
    print("new a", a)

'''

'''
