import numpy as np

DIRECTION = [(0, 1), (-1, 0), (0, -1), (1, 0)]
SIZE = 71
ITERATIONS = 1024
FILE = "input18"
# SIZE = 7
# ITERATIONS = 12
# FILE = "testinput18"


def traverse(field):
    seen = np.full(shape=field.shape, fill_value=False)

    distances = np.full(shape=field.shape, fill_value=np.inf)
    distances[1, 1] = 0

    while (
        min_dist := np.min((masked := np.ma.masked_where(seen, distances)))
    ) < np.inf:
        x, y = [a[0] for a in np.where(masked == min_dist)]
        seen[(x, y)] = True

        dist = distances[x, y]
        if (x, y) == (SIZE, SIZE):
            return int(dist)

        for dx, dy in DIRECTION:
            if field[x + dx, y + dy] == 0 and not seen[x + dx, y + dy]:
                distances[x + dx, y + dy] = min(dist + 1, distances[x + dx, y + dy])

    return False


def check_reachable(field):
    q = [(1, 1)]
    seen = {}
    while q:
        x, y = q.pop()
        if x == SIZE and y == SIZE:
            return True
        seen[(x, y)] = True
        for dx, dy in DIRECTION:
            if (x + dx, y + dy) not in seen and field[x + dx, y + dy] == 0:
                q.append((x + dx, y + dy))
    return False


def part_2(puzzle_input):
    field = np.full(shape=(SIZE, SIZE), fill_value=0)
    rows = puzzle_input.split("\n")
    for i in range(ITERATIONS):
        x, y = [int(x) for x in rows[i].split(",")]
        field[x, y] = 1
    field = np.pad(field, 1, "constant", constant_values=1)

    for i in range(ITERATIONS, len(rows)):
        print(i)
        x, y = [int(x) for x in rows[i].split(",")]
        field[x + 1, y + 1] = 1
        if not check_reachable(field):
            return f"{x},{y}"


with open(FILE) as f:
    puzzle_input = f.read()

field = np.full(shape=(SIZE, SIZE), fill_value=0)

count = 0
for row in puzzle_input.split("\n"):
    x, y = [int(x) for x in row.split(",")]
    field[x, y] = 1
    count += 1
    if count == ITERATIONS:
        break
field = np.pad(field, 1, "constant", constant_values=1)

print("Part 1:", traverse(field))

print("Part 2:", part_2(puzzle_input))
