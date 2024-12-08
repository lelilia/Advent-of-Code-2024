with open("input7") as f:
    puzzle_input = f.read()


def part_1(target, values):
    paths = [values.pop(0)]
    new_paths = []
    while values:
        number = values.pop(0)
        for n in paths:
            if n > target:
                continue
            new_paths.append(n * number)
            new_paths.append(n + number)
        paths = new_paths
        new_paths = []

    for path in paths:
        if path == target:
            return target
    return 0


def part_2(target, values):
    paths = [values.pop(0)]
    new_paths = []
    while values:
        number = values.pop(0)
        for n in paths:
            if n > target:
                continue

            new_paths.append(n * number)
            new_paths.append(n + number)
            new_paths.append(int(str(n) + str(number)))
        paths = new_paths
        new_paths = []

    for path in paths:
        if path == target:
            return target
    return 0


res = 0
res_2 = 0
for puzzle in puzzle_input.split("\n"):

    test_value, puzzle = puzzle.split(": ")

    test_value = int(test_value)
    values = [int(x) for x in puzzle.split(" ")]

    target = test_value
    res += part_1(test_value, values.copy())
    res_2 += part_2(test_value, values.copy())

print("Part 1:", res)

print("Part 2:", res_2)


assert part_1(190, [10, 19]) == 190
assert (res := part_1(3267, [81, 40, 27])) == 3267, f"Expected 3267, got {res}"
