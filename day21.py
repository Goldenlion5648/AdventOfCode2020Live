from collections import *
from math import *

with open("input21.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")


for x, ele in enumerate(a):
    a[x] = a[x].split(' (')
    a[x][1] = a[x][1][:-1]
    a[x][1] = a[x][1].split(" ")[1:]
    for i in range(len(a[x][1])):
        a[x][1][i]= "".join([j for j in a[x][1][i] if j != ","])
print(a)
allIng = set()
aller = set()
for j in a:
    allIng |= set(j[0].split(" "))
    aller |= set(j[1])

connections = []

for i in a:
    connections.append([set(i[0].split(" ")), set(i[1])])
print("connections", connections)
foodToAllergen = dict()
potentials = defaultdict(set)
scores = defaultdict(Counter)
tossed = set()
for i in connections:
    for j in i[0]:
        potentials[j] |= set(i[1])
print("potentials", potentials)
for j in connections:
    print(j)
    for i in j[0]:
        for k in j[1]:
            scores[i][k] += 1

            # pass
print(scores)
finalAllergies = dict()
allergenToFood = defaultdict(Counter)
for i in connections:
    for j in i[1]:
        for k in i[0]:
            allergenToFood[j][k] += 1

print("allergenToFood", allergenToFood)
changed = True
while changed:
    changed = False
    for i in allergenToFood:
        common = allergenToFood[i].most_common(2)
        print(common)
        if len(common) > 1 and common[0][1] == common[1][1]:
            continue
        finalAllergies[i] = common[0][0]
        for j in allergenToFood:
            if common[0][0] in allergenToFood[j]:
                allergenToFood[j].pop(common[0][0])
                # print("popping", common[0][0])
    temp = allergenToFood.copy()
    for final in finalAllergies:
        if final in temp:
            temp.pop(final)
    if allergenToFood != temp:
        allergenToFood = temp.copy()
        changed = True
    # break
print("allIng", allIng)
print(len(allIng))
safeFoods = allIng
safeFoods -= set(finalAllergies.values())

print("safeFoods", safeFoods)
answer=  0
for i in connections:
    answer += len(i[0] & safeFoods)

print("part1:", answer)
print("finalAllergies", finalAllergies)
part2Answer = []
for i in finalAllergies:
    part2Answer.append((i, finalAllergies[i]))
part2Answer.sort()
print("part2", ",".join(j[1] for j in part2Answer))

# print("new scores", scores)
# print("allergenToFood", allergenToFood)

# print("finalAllergies", finalAllergies)

# print("do not contain: kfcds, nhms, sbzzf, or trh")
'''

defaultdict(<class 'collections.Counter'>, {'sqjhc': Counter({'fish': 2, 'dairy': 1, 'soy': 1}), 'nhms': Counter({'fish': 1, 'dairy': 1}), 'kfcds': Counter({'fish': 1, 'dairy': 1}), 'mxmxvkd': Counter({'fish': 2, 'dairy': 2}), 'trh': Counter({'dairy': 1}), 'sbzzf': Counter({'dairy': 1, 'fish': 1}), 'fvjkl': Counter({'dairy': 1, 'soy': 1})})
new scores defaultdict(<class 'collections.Counter'>, {'sqjhc': Counter({'fish': 1, 'dairy': 0, 'soy': 0}), 'nhms': Counter({'fish': 0, 'dairy': 0}), 'kfcds': Counter({'fish': 0, 'dairy': 0}), 'mxmxvkd': Counter({'fish': 1, 'dairy': 1}), 'trh': Counter({'dairy': 0}), 'sbzzf': Counter({'dairy': 0, 'fish': 0}), 'fvjkl': Counter({'dairy': 0, 'soy': 0})})

connections [[{'sqjhc', 'kfcds', 'mxmxvkd', 'nhms'}, {'dairy', 'fish'}], [{'fvjkl', 'trh', 'mxmxvkd', 'sbzzf'}, {'dairy'}], [{'fvjkl', 'sqjhc'}, {'soy'}], [{'mxmxvkd', 'sqjhc', 'sbzzf'}, {'fish'}]]

potentials defaultdict(<class 'set'>, {'sqjhc': {'dairy', 'soy', 'fish'}, 'kfcds': {'dairy', 'fish'}, 'mxmxvkd': {'dairy', 'fish'}, 'nhms': {'dairy', 'fish'}, 'fvjkl': {'dairy', 'soy'}, 'trh': {'dairy'}, 'sbzzf': {'dairy', 'fish'}})'''
# for i in potentials:

    # if len(potentials[i]) >= 2:


# for i in range(len(connections)):
#     print("end", connections[i])
#     for j in connections[i][0]:
#         for k in connections:
#             if j in k[0] and len(connections[i][1] & k[1]) == 0:
#                 tossed.add(j)
# print(tossed)

# kfcds, nhms, sbzzf, or trh
        # 
# print(allIng)
# for j in allIng:
#     scores[j] = aller 
# print("scores", scores)
# answer =defaultdict(Counter)
# for i in a:
#     cur = i[0].split(" ")
#     for j in cur:
#         print("score j", j, scores[j])
#         print(scores[j] & set(i[1]))
#         # answer[j][scores[j] & set(i[1])] += 1
#         print("i[1]", i[1])

# print(scores)
# print(answer)
