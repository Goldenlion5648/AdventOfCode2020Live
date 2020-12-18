
'''

'''
from collections import *
from math import *
import copy
with open("input17.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

a = [list(x) for x in a]
newSize = 40
if len(a) % 2 != 0:
    newSize += 1 
for i in range(len(a)):
    a[i] = list('.' * ((newSize - len(a)) //2)) + a[i] + list('.' * ((newSize - len(a))//2))

while len(a) < newSize:
    a.insert(0, list('.' * newSize))
    a.append(list('.' * newSize))

print(a)

dim = len(a)
print("dim", dim)

numLayers = 24
layers = [[[["." for z in range(dim)] for i in range(dim)] \
for j in range(numLayers)] for q in range(numLayers)]

layers[numLayers//2][numLayers//2] = copy.deepcopy(a)
# print("layers", layers)

# assert False
def countNeighbors(layers2, x, y, z, w):
    count = 0
    for m in range(-1, 2):
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if i == j and j == k and k == 0 and m == 0:
                        continue
                    if dim > x + k >= 0 and dim > y + j >= 0 and \
                    numLayers > z + i >= 0 and numLayers > w + m >= 0:
                        try:
                            if layers2[w+m][z+i][y+j][x+k] == "#":
                                count += 1
                        except:
                            print([w+m, z+i, y+j, x+k])


    # print(z, y, x, "neighbors", count)
    return count

temp = []
for i in layers:
    temp.append(copy.deepcopy(i))

# print("temp", temp)
print("temp again")
for i in temp:
    for j in i:
        for k in j:
        # answer += j.count("#")
            print("".join(k))
    print()


for turns in range(6):
    for q in range(numLayers):
        for z in range(numLayers):
            for i in range(dim):
                for j in range(dim):
                    neighs = countNeighbors(layers, j, i, z, q)
                    # print(z, i, j, neighs)
                    if layers[q][z][i][j] == "#" and neighs not in [2, 3]:
                        temp[q][z][i][j] = "."
                        # print(z, i, j, "changed")
                    elif layers[q][z][i][j] == "." and neighs == 3:
                        temp[q][z][i][j] = "#"
                        # print("changed")
                        # print(z, i, j, "changed")

    # print(temp)
    print("after time", turns+1)
    # for i in temp:
    #     for j in i:
    #         # answer += j.count("#")
    #         print("".join(j))
    #     print()
    layers = copy.deepcopy(temp)

print()
answer = 0
# for i in layers:
#     for j in i:

for i in temp:
    for j in i:
        for k in j:
            answer += k.count("#")
            # print("".join(k))
    print()
print(answer)
        # if 

'''

'''
