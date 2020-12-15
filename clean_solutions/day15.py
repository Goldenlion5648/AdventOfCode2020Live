from collections import *

with open("input15.txt") as f:
    a = list(map(int,f.read().strip().split(",")))

def solve(maxTurn, a):
    said = defaultdict(list)
    nums = deque()
    for x, ele in enumerate(a):
        said[ele].append(x+1)
        nums.append(ele)

    # print(nums)
    recent = a[-1]
    turn = len(a) + 1
    while turn < maxTurn + 1:
        # if turn % 10000 == 0:
        #     print(turn)
        if len(said[recent]) == 1:
            app = 0
            nums.append(app)
            said[app].append(turn)
        elif len(said[recent]) == 0:
            app = 0
            nums.append(app)
            said[app].append(turn)
        else:
            app = said[recent][-1] - said[recent][-2]
            nums.append(app)
            said[app].append(turn)
        turn += 1
        recent = app

    return nums[-1]

#recommend using pypy
print("part 1:", solve(2020, a))
print("part 2:", solve(30000000, a))