
'''
acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
'''
from collections import *

with open("input8.txt") as f:
    a = f.read().strip().split("\n")

a = [i.split() for i in a]
for i in range(len(a)):
    a[i][1] = int(a[i][1])

pos = 0
acc = 0
seen = set()
while pos not in seen:
    seen.add(pos)
    if a[pos][0] == "acc":
        acc += a[pos][1]
        pos += 1
    elif a[pos][0] == "jmp":
        pos += a[pos][1]
    else:
        pos += 1
    if pos == len(a):
        shouldStop = True
        break
# print(a)
print("part 1:",acc)

changePos = 0
shouldStop = False
while not shouldStop:
    # print(changePos)
    if a[changePos][0] == "jmp":
        a[changePos][0] = "nop"
    elif a[changePos][0] == "nop":
        a[changePos][0] = "jmp"
    seen = set()
    pos = 0
    acc = 0
    while pos not in seen:
        seen.add(pos)
        if a[pos][0] == "acc":
            acc += a[pos][1]
            pos += 1
        elif a[pos][0] == "jmp":
            pos += a[pos][1]
        else:
            pos += 1
        if pos == len(a):
            shouldStop = True
            break
    else:
        if a[changePos][0] == "jmp":
            a[changePos][0] = "nop"
        elif a[changePos][0] == "nop":
            a[changePos][0] = "jmp"
        changePos += 1

print(acc)
'''

'''
