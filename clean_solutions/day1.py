
'''

'''
from collections import *

with open("input1.txt") as f:
    a = list(map(int,f.read().strip().split("\n")))
    # a = f.read().strip().split("\n")

#part 1
def part1():
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if a[i] + a[j] == 2020:
                    print("part 1", a[i] * a[j])
                    return

def part2():
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if a[i] + a[j] + a[k] == 2020:
                    print("part 2", a[i] * a[j] * a[k])
                    return

part1()
part2()