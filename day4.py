
'''

'''
from collections import *
import re

with open("input4.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n\n")

# a = [i for i in a if i != ""]
# print(a)
count = 0
required = ["byr:",
"iyr:", 
"eyr:", 
"hgt:",
"hcl:", 
"ecl:", 
"pid:"]
valid = []
for i in a:
    works = True
    # print("i", i)
    for j in required:
        # print(j)
        ran = True
        if j not in i:
            works = False
            break
    if works and ran:
        count += 1
        valid.append(i)
        # print("added")

print("part 1", count)
# print(valid)
count = 0
for j in valid:
    # b = dict.fromkeys(i)
    # v = i.replace(":", "=")
    # v =v.replace(" ", ",")
    # b = dict(v)
    c = dict()
    i  =j.replace("\n", " ").strip()
    cur = 0
    # print(i)
    while cur < len(i):
        try:
            prop = i.index(" ", cur)
        except:
            k = i[cur:].split(":")
            # print("k", k)
            k, v = k[0], k[1]
            cur = prop + 1
            c[k] = v
            break
        k = i[cur:prop].split(":")
        # print("k", k)
        k, v = k[0], k[1]
        cur = prop + 1
        c[k] = v

    # print(c)
    c["byr"] = int(c["byr"])
    if not (1920 <= c["byr"] <= 2002):
        continue
    c["iyr"] = int(c["iyr"])
    if not (2010 <= c["iyr"] <= 2020):
        continue
    c["eyr"] = int(c["eyr"])
    if not (2020 <= c["eyr"] <= 2030):
        continue
    if c["hgt"][0].isdigit():
        if c["hgt"].endswith("cm"):
            # print("-----------------", int(c["hgt"][0:-2]))
            if 150 <= int(c["hgt"][0:-2]) <= 193:
                pass
            else:
                continue

        elif c["hgt"].endswith("in"):
            if 59 <= int(c["hgt"][0:-2]) <= 76:
                pass
            else:
                continue
        else:
            continue
    else:
        continue

    hair = c["hcl"]
    if c["hcl"].startswith("#"):
        works2 = True
        works2 = all([x for x in c["hcl"][1:] if x.isdigit() or x in ["a", "b", "c", "d", "e", "f"]])
        if works2 == False:
            continue
    else:
        continue

    if c["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    if len(c["pid"]) == 9 and c["pid"].isdigit():
        pass
    else:
        continue

    # print("added")
    count += 1
    # print(b)

print("part 2:", count)
'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.'''