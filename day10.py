import numpy as np

NEIGHBORS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part_1(puzzle):
    starting_points = np.where(puzzle == 0)
    starts = list(zip(starting_points[0], starting_points[1]))
    res = 0
    for (x, y) in starts:
        seen = {}
        q = [(x, y)]
        while q:
            x, y = q.pop()
            if (x, y) in seen:
                continue
            seen[(x, y)] = True
            value = puzzle[x, y]
            if value == 9:
                res += 1
            for (dx, dy) in NEIGHBORS:
                if puzzle[x + dx, y + dy] == value + 1:
                    q.append((x + dx, y + dy))
    return res


def part_2(puzzle):
    starting_points = np.where(puzzle == 0)
    starts = list(zip(starting_points[0], starting_points[1]))
    res = 0
    for (x, y) in starts:
        q = [(x, y)]
        while q:
            x, y = q.pop(0)
            value = puzzle[x, y]
            if value == 9:
                res += 1
            for (dx, dy) in NEIGHBORS:
                if puzzle[x + dx, y + dy] == value + 1:
                    q.append((x + dx, y + dy))
    return res


with open("input10") as f:
    puzzle = f.read()

puzzle = np.array([[int(x) for x in y] for y in puzzle.split("\n")])
puzzle = np.pad(puzzle, 1, "constant", constant_values=-1)


print("Part 1:", part_1(puzzle))
print("Part 2:", part_2(puzzle))
