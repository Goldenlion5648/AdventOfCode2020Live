
'''

'''
from collections import *

class ticketField():
    def __init__(self, field, r1, r2):
        self.field = field
        self.r1 = r1
        self.r2 = r2

with open("input16.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n\n")

# print(a)
fields = []
a[0] = a[0].split("\n")
# print(a)
for i in a[0]:
    name, rs = i.split(": ")
    rs = rs.split(" or ")
    r1, r2 = [list(map(int, x.split("-"))) for x in rs]
    # print(r1, r2)
    fields.append(ticketField(name, r1, r2))

a[2] = a[2].split("\n")
# print(a[2])
nearbyTickets = [list(map(int, x.split(","))) for x in a[2][1:]]
# print(nearbyTickets) 
# rules = []
# for i in a:
#     rules.append(i[i.index(":")+2:].split(" or "))

# ranges = [[45, 535], [550, 961], [45, 278], [294, 974], [46, 121], [138, 965], [38, 149], [173, 949], [34, 223], [248, 957], [32, 64], [79, 952], [49, 879], [905, 968], [47, 306], [323, 973], [46, 823], [834, 971], [30, 464], [486, 963], [40, 350], [372, 965], [47, 414], [423, 950], [45, 507], [526, 956], [42, 779], [799, 970], [26, 865], [872, 955], [43, 724], [739, 970], [25, 914], [926, 958], [33, 205], [218, 965], [43, 101], [118, 951], [45, 844], [858, 970]]

keep = []
count = 0
contam = False
for ticket in nearbyTickets:
    # cur = list(map(int, i.split(",")))
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
# print(keep)
# print(len(keep))


# keep = 

# def explore(order):
#     for i in 

# order = dict()
# def explore(found):
    # ticketPos = 0
    # rangePos= 0
found = dict()
fringe = []
possibleValues = defaultdict(list)
# while True:
for i in fields:
    # print(i.field)
    # if i.field in found:
    #     continue
    # temp = found.copy()
    # print("len", len(keep[0]))
    valids = []
    for z in range(len(keep[0])):
        # print(i.r1[0], keep[z][j])
        curTest = [(i.r1[0] <= keep[j][z] <= i.r1[1]) or \
            (i.r2[0] <= keep[j][z] <= i.r2[1]) for j in \
            range(len(keep))]
        # print("cur", curTest)
        works = all(curTest)
        # print("works", works)
        if works:
            possibleValues[i.field].append(z)
    # possibleValues.append(valids)

        # curFieldWorks = 
        # print("curFieldWorks", curFieldWorks)
# print(possibleValues)
maxCount = 1
# for j in possibleValues:
#     maxCount *= len(possibleValues[j])
# print(maxCount)
# needed = [i for i in range(20)]
newPossible = [[i, set(possibleValues[i])] for i in possibleValues]
newPossible.sort(key=lambda x: len(x[1]))
# print(newPossible)
remaining = {i for i in range(20)}
realValues = dict()
for i in newPossible:
    realValues[i[0]] = i[1] & remaining
    remaining ^= realValues[i[0]]
# print(realValues)
# print(a)
myTicket = list(map(int, a[1][a[1].index(":\n")+2:].split(",")))
# print(myTicket)
answer = 1
for i in realValues:
    if i.startswith("departure"):
        answer *= myTicket[realValues[i].pop()]
print("part 2", answer)

# for value in range(20):
#     for f in possibleValues:
#         if 

        # assert False
        # if works:
            # temp[i] = 

        # for j in 

    # while ticketPos < len(validTickets[0]):
    #     while rangePos < len(ranges):
    #         works = all([(ranges[rangePos][0] <= x[ticketPos] <= ranges[rangePos][1]) or (ranges[rangePos+1][0] <= x[ticketPos] <= ranges[rangePos+1][1]) for x in validTickets])
    #         rangePos += 2
    #         print(works)
    #         if works:
    #             temp = order.copy()
    #             temp.add()
    #             explore()
    #     ticketPos += 1
    # if works:


# for i in validTickets:
#     added = False
#     pos = 0
#     while True:
#         while not added:
#             if not(ranges[pos][0] <= i[ticketPos] <= ranges[pos][1]):
#                 pos += 1
#                 break
#         else
#     ticketPos += 1
