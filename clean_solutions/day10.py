
with open("input10.txt") as f:
    a = list(map(int,f.read().strip().split("\n")))

a.sort()
a = [0] + a + [a[-1] + 3]
# print(a)
highest = max(a) + 3
oneDif = 0
threeDif = 0
for i in range(len(a) - 1):
    if abs(a[i]-a[i+1]) == 3:
        threeDif += 1
    elif abs(a[i]-a[i+1]) == 1:
        oneDif += 1

# print(oneDif)
# print(threeDif)
print("part 1", oneDif * threeDif)

mem = []
pos = len(a) - 1
mem = [0 for i in range(len(a))]
mem[-1] = 1
while pos >= 0:
    i= pos
    temp = 0
    for j in range(1, 4):
        if i + j >= len(a):
            break
        for k in range(1, 4):
            if a[i]+ k == a[i + j]:
                temp += 1
                mem[i] += mem[i+j]

    pos -= 1
# print(mem)

print("part 2", mem[0])
