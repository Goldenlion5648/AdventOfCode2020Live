
'''

'''
from collections import *

with open("input7.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

q = defaultdict(list)
for i in a:
    cur = i.replace("bags", "").replace("bag", "").replace(" .", "").split(" ")
    # c = i.index("bags") + 4
    # x = c + 9
    # cur = list(map(strip, cur))
    q[tuple(cur[0:2])] = (" ".join(cur[4:]).strip().split(","))
print(q)

has = {"shiny gold"}
seen = set()
updated = True
oldSize = 0
cost = 0
while updated:
    updated = False
    for i in q:
        curString = "".join(q[i])
        # print("cur", curString)
        print(i, q[i])
        temp = set()
        for j in q[i]:
            for x in has:
                if x in j:
                    temp.add(" ".join(i))
                    updated = True
        
        has |= temp
    if oldSize != len(has):
        oldSize = len(has)
    else:
        updated = False
        break
    print("has", has)
        # for j in has:
        #     print("j", "".join(j))
        #     print("cur2", curString)
        #     if j in curString and i not in has:
        #         temp.add(i) 
        #         updated = True

        # has = temp

print("part 1", len(has) - 1)

# for i in q:
#     q[i] = list(map(tuple, q[i]))
part2Dict = defaultdict(dict)
for i in q:
    for j in q[i]:
        curBag = j.strip().split()
        try:
            count = int(curBag[0])
            curBagName = "".join(curBag[1:])
        except:
            count = 0
            curBagName = "".join(curBag)
        part2Dict["".join(i).strip()][curBagName] = count
# print(q)
print(part2Dict)
# print(q)
# def search(start, curCost):
#     print("start", start)
#     print("cost", curCost)
#     newName2 = start
#     # if type(start) is not tuple:
#     if " " in start:
#         newName2 = tuple(start[start.index(" ", 1) + 1:].strip().split())
#     for z in q[newName2]:
#         newName = tuple(z[z.index(" ", 1) + 1:].strip().split())
#         print("new", newName)
#         if newName in q:
#             curCost *= search(newName, curCost)
#         pass
#     return curCost

fringe = [{"shinygold": 1}]
prev = 1
totalCost = 0
bagCounts = Counter()
while len(fringe) > 0:
    cur= fringe.pop()
    # print("cur",cur)
    for i in cur:
        bagCounts[i] += cur[i]
        for j in range(cur[i]):
            fringe.append(part2Dict[i])
    # print("fringe", fringe)
    # print("bagCounts", bagCounts)

bagCounts.pop("shinygold")
print("part 2:", sum(bagCounts.values()))



'''
1 shiny
2 dark red
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
'''
