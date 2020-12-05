with open("input5.txt") as f:
    a = f.read().strip().split("\n")

seats = []
for i in a:
    #convert to binary
    cur = i[0:7].replace("F", "0").replace("B", "1")
    end = i[7:].replace("R", "1").replace("L", "0")
    seats.append((int(cur, 2), int(end, 2)))
#get largest beginning id
b = (max(seats, key = lambda x: x[0]))
print("part 1", b[0] * 8 + b[1])

#part 2
seats.sort()
#make list of all seat ids
seat_nums = []
for i in seats:
    seat_nums.append((i[0] * 8 + i[1]))

x = seat_nums[0]
for i in range(1, len(seat_nums)):
    #if missing, its the answer
    if seat_nums[i] - 1 != x:
        print("part 2", seat_nums[i] - 1)
        break
    x = seat_nums[i]