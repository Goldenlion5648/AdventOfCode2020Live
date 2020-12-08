with open("input8.txt") as f:
    a = f.read().strip().split("\n")

a = [i.split() for i in a]
for i in range(len(a)):
    a[i][1] = int(a[i][1])

def run_machine(instructions):
    pos = 0
    acc = 0
    seen = set()
    finished = False
    while pos not in seen:
        seen.add(pos)
        if instructions[pos][0] == "acc":
            acc += instructions[pos][1]
            pos += 1
        elif instructions[pos][0] == "jmp":
            pos += instructions[pos][1]
        else:
            pos += 1
        if pos == len(a):
            finished = True
            break
    return acc, finished

print("part 1:", run_machine(a)[0])

def flip(pos, a):
    if a[pos][0] == "jmp":
        a[pos][0] = "nop"
    elif a[pos][0] == "nop":
        a[pos][0] = "jmp"
    return a

changePos = 0
shouldStop = False
while not shouldStop:
    a = flip(changePos, a)

    score, finished = run_machine(a)
    if finished == False:
        a = flip(changePos, a)
        changePos += 1
    else:
        break

print("part 2", score)
