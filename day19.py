FILE = "testinput19"
FILE = "input19"


def check_possible(towles, pattern, length):
    q = [pattern]
    while q:
        curr = q.pop(0)

        for i in range(1, length+1):
            if curr[:i] in towles:
                if i == len(curr):
                    return True
                if curr[i:] not in q:
                    q.append(curr[i:])
    return False

def check_possible_part_2(towles, pattern, length):
    q = [pattern]
    count = 0
    times = {}
    times[pattern] = 1
    while q:
        curr = q.pop(0)
        for i in range(1, min(length+1, len(curr)+1)):
            if curr[:i] in towles:
                if i == len(curr):
                    count += times[curr]
                    continue
                elif curr[i:] not in q:
                    times[curr[i:]] = times[curr]
                    q.append(curr[i:])
                else:
                    times[curr[i:]] += times[curr]
        # print(curr, q, times, "\n")
    return count

with open(FILE) as f:
    puzzle_input = f.read()

towles, patterns = puzzle_input.split("\n\n")
towles = towles.split(", ")
patterns = patterns.split("\n")

# print(towles)

letters = {}
for i, towle in enumerate(towles):
    for char in towle:
        if char in letters:
            letters[char].append(i)
        else:
            letters[char] = [i]
# print (letters)

towle_dict = {}
length = 0
for towle in towles:
    towle_dict[towle] = True
    length = max(length, len(towle))

count = 0
for pattern in patterns:
    # print(pattern)
    if check_possible(towle_dict, pattern, length):
        count += 1

print("Part 1:", count)

# print(check_possible(towle_dict, "bwurrg", length))

# print(check_possible(towle_dict, "gburgrwbgubggbgggrburbwwwbggrbbwrbubbwrgggbwwwururwugwubugrw", length))

count = 0
for pattern in patterns:
    count +=  check_possible_part_2(towle_dict, pattern, length)
    print(pattern, count)
print("Part 2:", count)

# print(check_possible_part_2(towle_dict, "rrbgbr", length))