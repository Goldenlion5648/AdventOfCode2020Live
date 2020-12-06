    with open("input6.txt") as f:
        a = f.read().rstrip().split("\n\n")

    def part1(a):
        a = a.copy()
        for i in range(len(a)):
            a[i] = set(list(a[i]))
            a[i] = set([j for j in a[i] if j != '\n'])

        total = 0
        cur = a[0]
        for i in a:
            total += len(i)
            cur ^= i
        print("part 1", total)

    def part2(a):
        total = 0
        a = a.copy()
        for i in a:
            cur = i.split("\n")
            x = set(list(cur[0]))
            for j in range(len(cur)):
                x &= set(list(cur[j]))
            total += len(x)
        print("part 2", total)

    part1(a)
    part2(a)
