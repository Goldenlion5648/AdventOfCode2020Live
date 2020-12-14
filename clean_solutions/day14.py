with open("input14.txt") as f:
    a = f.read().strip().split("\n")
mem = dict()
line = 0
cur = list('0' * 36)
print("cur", cur)

while True:

    if "mask" in a[line]:
        mask = a[line].split()[-1]
        line += 1
        print("mask\n", mask)
    while line < len(a) and "mem" in a[line]:
        # exec(a[line])
        b = a[line].split()
        value = int(b[-1])
        num = int(b[-1])
        c = bin(num)[2:]
        c = "0" * (36 - len(c)) + c
        addressAsBin = bin(int(b[0][4:-1]))[2:]
        address = "0" * (36 - len(addressAsBin)) + addressAsBin
        flips = []
        address = list(address)
        for x, ele in enumerate(address):
            if mask[x] == "X":
                flips.append(x)
                address[x] = mask[x]
            # if mask[x] != "X":
            elif mask[x] == "1":
                address[x] = mask[x]
            else:
                # address[x] = c[x]
                pass
        print("flips", flips)
        curString = "".join(address)
        maxN = 2**len(flips)
        binStrings = []
        for i in range(maxN):
            binNum = bin(i)[2:]
            # print("binNum", binNum)
            bina = '0' * (len(bin(maxN-1)[2:]) - len(binNum)) + binNum
            # print(bina)
            binStrings.append(bina)
        curPos = 0
        # print("before address", address)
        print(len(address))
        while curPos < len(binStrings):
            curBinSplit = list(binStrings[curPos])
            for j in range(len(flips)):
                address[flips[j]] = curBinSplit[j]
            tryPos =int("".join(address), 2)
            print("attempting", tryPos)
            mem[tryPos] = value
            curPos += 1

        line += 1
    if line >= len(a):
        break 

# print(mem)
print(sum(mem.values()))


'''

'''
