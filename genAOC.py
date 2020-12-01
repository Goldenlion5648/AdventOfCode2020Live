'''Code by Colter
'''
import argparse
import os
import sys

parser = argparse.ArgumentParser(
    description=
    "generates Advent of Code template files")
parser.add_argument("-d", "--dayNum")


args = parser.parse_args()

day = str(args.dayNum)
# if len(day) < 2:
#     day = '0'+day

template = f'''
from collections import *

with open("input{day}.txt") as f:
    a = list(map(int,f.read().strip().split("\\n")))
    # a = f.read().strip().split("\\n")



'''

with open(f"day{day}.py", 'w') as f:
    f.write(template)
with open(f"input{day}.txt", 'w') as f:
    pass

