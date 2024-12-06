import numpy as np

DIRECTIONS = ["^", ">", "v", "<"]

STEPS = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}

with open("input6") as f:
    puzzle_input = f.read()


def part_1(obsticals, puzzle_map, index):
    seen = {}

    guard_x, guard_y = guard_up[0][0], guard_up[1][0]

    while True:
        seen[(guard_x, guard_y)] = index

        dx = STEPS[DIRECTIONS[index]][0]
        dy = STEPS[DIRECTIONS[index]][1]
        if guard_x + dx < 0 or guard_x + dx >= puzzle_map.shape[0]:
            return len(seen), seen
        if (guard_x + dx, guard_y + dy) in obsticals:
            index = (index + 1) % 4
        else:
            guard_x += dx
            guard_y += dy


def part_2(obsticals, x, y, index):
    seen = {}
    while True:
        if (x, y, index) in seen:
            # print(seen)
            return True, seen
        seen[(x, y, index)] = True

        dx = STEPS[DIRECTIONS[index]][0]
        dy = STEPS[DIRECTIONS[index]][1]

        if (
            x + dx < 0
            or x + dx >= puzzle_map.shape[0]
            or y + dy < 0
            or y + dy >= puzzle_map.shape[1]
        ):
            return False, seen
        if (x + dx, y + dy) in obsticals:
            index = (index + 1) % 4
        else:
            x += dx
            y += dy


puzzle_map = np.array([[y for y in x] for x in puzzle_input.split("\n")])


# guard = np.where([puzzle_map == "^" or puzzle_map == ">" or puzzle_map == "<" or puzzle_map == "v"])
guard_up = np.where(puzzle_map == "^")
index = 0

STEPS = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}


obsticals_map = np.where(puzzle_map == "#")
obsticals = {}
for ox, oy in zip(obsticals_map[0], obsticals_map[1]):

    obsticals[(ox, oy)] = True

# print(part_1(obsticals, puzzle_map, index))

part_1_res, path = part_1(obsticals, puzzle_map, index)

print(part_1_res)

x, y = guard_up[0][0], guard_up[1][0]

print(part_2(obsticals, x, y, index)[0])

# print(path.keys())
res = 0
for p_x, p_y in path.keys():
    if p_x == x and p_y == y:
        continue
    new_obsticals = obsticals.copy()
    new_obsticals[(p_x, p_y)] = True
    if part_2(new_obsticals, x, y, index)[0]:
        res += 1
print(res)
