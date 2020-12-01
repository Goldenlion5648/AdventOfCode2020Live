
'''

'''
from collections import *

with open("input1.txt") as f:
    a = list(map(int,f.read().strip().split("\n")))
    # a = f.read().strip().split("\n")

for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if a[i] + a[j] + a[k] == 2020:
                print(a[i] * a[j] * a[k])
test 1 2 three