from collections import *
from math import *

with open("input25.txt") as f:
    a = list(map(int,f.read().strip().split("\n")))
    # a = f.read().strip().split("\n")

subNum = 7
cardPubKey, doorPubKey = a
# cardPubKey, doorPubKey = 5764801, 17807724

# cardPubKey = 5764801
loops = []
loop = 0
val = 1
while val != cardPubKey:
    val *= subNum
    val = val % 20201227
    loop += 1
print("loop", loop)
loops.append(loop)
loop = 0
val = 1
while val != doorPubKey:
    val *= subNum
    val = val % 20201227
    loop += 1
print(loop)
loops.append(loop)
val = 1
subNum = doorPubKey
for i in range(loops[0]):
    val *= subNum
    val = val % 20201227
print(val)

subNum = cardPubKey
val = 1
for i in range(loops[1]):
    val *= subNum
    val = val % 20201227
print(val)