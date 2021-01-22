from collections import *
from math import *
import re

with open("input19.txt") as f:
    a = f.read().strip().split("\n")

# a.sort()
begin= a[:a.index("")]
samples = a[a.index("")+1:]
# samples = 
begin.sort()
rules = defaultdict(list)



for i in begin:
    print(i)
    num, cur = i.split(": ")
    # print("num", num)
    # print("cur", cur)
    cur = cur.replace("\"", "")
    # num = int(num)
    # cur = cur.split(" | ")
    pipeIn = "|" in cur
    # if pipeIn:
    # cur = list(cur)
    # print("cur===============", cur)
    # print("new cur===========================", cur)
    # cur = cur.replace(" ", "")
    cur = cur.split(" ")
    letterPos = 0
    # if num == "11":
    #     x = 1
    #     while x < len(cur):
    #         cur.insert(x, "(")
    #         cur.insert(x, ")")
    #         x += 3
    #     cur.insert(0, "((")
    #     cur.append("))")
        # cur.insert(3, "q")
        # print(cur)
        # assert False

    if num == "8":
        cur.insert(0, "(")
        cur.append(")")
        cur.append("+")
        # print(cur)

    elif pipeIn:
        z = 0
        while z < len(cur):
            if cur[z].isnumeric():
                cur.insert(z+1, ")")
                cur.insert(z, "(")
                z += 1
            elif cur[z] == "|":
                cur.insert(z+1, "(")
                cur.insert(z, ")")
                cur.insert(0, "(")
                cur.append(")")
                z += 2
            z += 1
        cur.insert(0, "(")
        cur.append(")")
    else:
        try:
            x = 1
            while x < len(cur):
                cur.insert(x, "(")
                cur.insert(x, ")")
                x += 3
            cur.insert(0, "((")
            cur.append("))")
        except:
            print("failed")
            assert False


        # assert False
    # if num == "11":
        #42

    if "\"" in cur[0]:
        rules[num].append(cur[0].replace("\"", ""))
    else:
        # print("new", cur)
        rules[num] += cur
print(rules)
print(len(rules))
letters = dict()
for key in rules:
    if any(j.isalpha() for j in rules[key]):
        letters[key] = rules[key]
print("new rules")
for i in rules:
    print(i, ":", rules[i])
print("before", letters)
changed = True
# letters["500"] = ["500"]

while changed:
    changed = False
    for key in rules:
        for char in range(len(rules[key])):
            # print("rules[key]", rules[key])
            # print("rules[key][char]", rules[key][char])
            # if rules[key][char] == "500":
            #     assert False
            if rules[key][char] in letters:
                if rules[key][char] == "11":
                    continue
                #     assert False
                rules[key][char:char+1] = letters[rules[key][char]]
                # if rules[key][char] != "500":
                #     changed = True

                if key not in letters:
                    letters[key] = rules[key]
                    # print("new letters", letters)
        # print(rules)

print(rules)
print("letter", letters)
rg = "".join(rules['0'])
rg = rg.replace(" ", "")
rg = "("+rg + ")"
rg = re.compile(rg)
print(rg)
answer = 0
for i in samples:
    # print(i)
    found = re.search(rg, i)
    # print(found)
    if found is not None and found.span() == (0, len(i)):
        # print("matched")
        answer += 1

print(answer)

