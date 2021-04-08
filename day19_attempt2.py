import re
with open("input19.txt") as f:
    a = f.read().strip().split("\n\n")

# print(a)
def get_rules_and_messages():

    rules = a[0].split("\n")
    messages = a[1].split("\n")
    # if part2:
    #     pos = 0
    #     while pos < len(rules):
    #         if rules[pos].startswith("8: 42 | 42 8")
    # print(rules)
    rules = [i.split(": ") for i in rules]
    return rules, messages

def get_conversions(rules, count=1, part2=False):
    conversions = dict()

    # if part2:
    # "8": "42 | 42 8", "11": "42 31 | 42 11 31"
    for rule in rules:
        conversions[rule[0]] = "( "+rule[1] +" )"
    if part2:
        part2_replacements = {"8": "( 42 )+", "11": "( 42 ){count} ( 31 ){count}".replace("count", str(count))}
        # print(part2_replacements)
        conversions.update(part2_replacements)
    # print(conversions)
    for i in conversions:
        if "|" in conversions[i]:
            cur = conversions[i].split("|")
            for j in range(len(cur)):
                cur[j] = "( " + cur[j] + " )"
            conversions[i] = "( " + " | ".join(cur) + " )"

    # print("after", conversions)
    #remove quotes
    for i in conversions:
        if '"' in conversions[i]:
            conversions[i] = conversions[i].replace('"', "")
    return conversions

def make_replacements(conversions):
    # global conversions
    changed = True
    while changed:
        changed = False
        for i in conversions:
            before = conversions[i]
            for num in conversions[i].split(" "):
                if num in conversions:
                    conversions[i] = conversions[i].replace(' ' + num + ' ', ' ' + conversions[num] + ' ')

            if before != conversions[i]:
                changed = True
    for i in conversions:
        conversions[i] = conversions[i].replace(" ", "")
    return conversions


def count_matches(conversions, messages):
    matches = 0
    matched_strings = set()
    for m in messages:
        pat_status = re.fullmatch(conversions['0'], m)
        if pat_status and pat_status.span()[1] - pat_status.span()[0] == len(m):
            # print("matched")
            matches += 1
            matched_strings.add(m)
    return matches, matched_strings

rules, messages = get_rules_and_messages()
conversions = get_conversions(rules)
conversions = make_replacements(conversions)

print("part 1:", count_matches(conversions, messages)[0])
maxVal = -1
matched_strings = set()
for i in range(1, 1000):
    rules, messages = get_rules_and_messages()
    conversions = get_conversions(rules, i, part2=True)
    conversions = make_replacements(conversions)
    # print(conversions["0"])
    matched_strings |= count_matches(conversions, messages)[1]
    # maxVal = max(maxVal, count_matches(conversions, messages))
print("part 2:", len(matched_strings))
