from collections import *

class ticketField():
    def __init__(self, field, r1, r2):
        self.field = field
        self.r1 = r1
        self.r2 = r2

with open("input16.txt") as f:
    a = f.read().strip().split("\n\n")

fields = []
a[0] = a[0].split("\n")
for i in a[0]:
    name, rs = i.split(": ")
    rs = rs.split(" or ")
    r1, r2 = [list(map(int, x.split("-"))) for x in rs]
    fields.append(ticketField(name, r1, r2))

a[2] = a[2].split("\n")
nearbyTickets = [list(map(int, x.split(","))) for x in a[2][1:]]

keep = []
count = 0
contam = False
for ticket in nearbyTickets:
    j = 0
    contam = False
    for ele in (ticket):
        found = False

        for crit in fields:
            # print("ranges", x[0], x[1])
            if crit.r1[0] <= ele <= crit.r1[1]:
                found = True
                # print("found")
                break
            elif crit.r2[0] <= ele <= crit.r2[1]:
                found = True
                # print("found")
                break
        if not found:
            count += ele
            contam = True
    if not contam:
        keep.append(ticket)
    j += 2

print("part 1", count)

found = dict()
fringe = []
possibleValues = defaultdict(list)
for i in fields:
    valids = []
    for z in range(len(keep[0])):
        curTest = [(i.r1[0] <= keep[j][z] <= i.r1[1]) or \
            (i.r2[0] <= keep[j][z] <= i.r2[1]) for j in \
            range(len(keep))]
        works = all(curTest)
        if works:
            possibleValues[i.field].append(z)

maxCount = 1
newPossible = [[i, set(possibleValues[i])] for i in possibleValues]
newPossible.sort(key=lambda x: len(x[1]))
remaining = {i for i in range(20)}

realValues = dict()
for i in newPossible:
    realValues[i[0]] = i[1] & remaining
    remaining ^= realValues[i[0]]

myTicket = list(map(int, a[1][a[1].index(":\n")+2:].split(",")))
answer = 1
for i in realValues:
    if i.startswith("departure"):
        answer *= myTicket[realValues[i].pop()]
print("part 2", answer)