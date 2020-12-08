from collections import *

with open("input7.txt") as f:
    a = f.read().strip().split("\n")

q = defaultdict(list)
for i in a:
    cur = i.replace("bags", "").replace("bag", "").replace(" .", "").split(" ")
    q[tuple(cur[0:2])] = (" ".join(cur[4:]).strip().split(","))
# print(q)

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
        # print(i, q[i])
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
    # print("has", has)

print("part 1", len(has) - 1)

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
# print(part2Dict)

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
