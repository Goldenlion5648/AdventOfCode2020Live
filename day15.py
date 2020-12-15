
'''

'''
from collections import *

with open("input15.txt") as f:
    a = list(map(int,f.read().strip().split(",")))
    # a = f.read().strip().split("\n")

said = defaultdict(list)
# d =deque(a)
# for j in range(2020):
turn = 4
    # for i, x in enumerate(a):
nums = deque()
for x, ele in enumerate(a):
    said[ele].append(x+1)
    nums.append(ele)


print(nums)
recent = a[-1]
turn = len(a) + 1
while turn < 30000000 + 1:
    if turn % 10000 == 0:
        print(turn)
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

# print(said)
# print(nums)
print(nums[-1])

# while turn <= 2020:
#     if len(said[recent]) == 0:
#         said[recent].append(0)
#         nums.append(0)

#     elif len(said[recent]) == 1:
#         said[recent].append(0)
#         nums.append(0)
#     recent = nums[-1]
#     turn += 1
#     print(said)
# print(nums)
        # print(i)
    # else:

# if d[-1]


'''

'''
