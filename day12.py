import numpy as np


def part_1(garden):
    seen = {}
    res = 0
    for start_x in range(1, garden.shape[0] - 1):
        for start_y in range(1, garden.shape[1] - 1):
            if (start_x, start_y) in seen:
                continue
            curr_fence = 0
            curr_area = 0
            q = [(start_x, start_y)]
            while q:
                (x, y) = q.pop(0)
                if (x, y) in seen:
                    continue
                seen[(x, y)] = True
                curr_area += 1

                for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if 0 <= x + dx < garden.shape[0] and 0 <= y + dy < garden.shape[1]:
                        if garden[x, y] == garden[x + dx, y + dy]:
                            q.append((x + dx, y + dy))
                        else:
                            curr_fence += 1
            res += curr_area * curr_fence
    return res


def part_2(garden):
    seen = {}
    res = 0
    for start_x in range(1, garden.shape[0] - 1):
        for start_y in range(1, garden.shape[1] - 1):
            if (start_x, start_y) in seen:
                continue
            fence = []
            curr_area = 0
            curr_sides = 0
            q = [(start_x, start_y)]
            while q:
                (x, y) = q.pop(0)
                if (x, y) in seen:
                    continue
                seen[(x, y)] = True
                curr_area += 1
                for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if 0 <= x + dx < garden.shape[0] and 0 <= y + dy < garden.shape[1]:
                        if garden[x, y] == garden[x + dx, y + dy]:
                            q.append((x + dx, y + dy))
                        else:
                            fence.append((x + dx / 10, y + dy / 10))

            while fence:
                curr = fence.pop(0)
                if curr[1] % 1 == 0:
                    # go up
                    i = 1
                    while (curr[0], curr[1] + i) in fence:
                        fence.remove((curr[0], curr[1] + i))
                        i += 1
                    i = -1
                    while (curr[0], curr[1] + i) in fence:
                        fence.remove((curr[0], curr[1] + i))
                        i -= 1

                    curr_sides += 1
                if curr[0] % 1 == 0:
                    i = 1
                    while (curr[0] + i, curr[1]) in fence:
                        fence.remove((curr[0] + i, curr[1]))
                        i += 1
                    i = -1
                    while (curr[0] + i, curr[1]) in fence:
                        fence.remove((curr[0] + i, curr[1]))
                        i -= 1

                    curr_sides += 1

            res += curr_area * curr_sides
    return res


with open("input12") as f:
    puzzle = f.read()

garden = np.array([[x for x in y] for y in puzzle.split("\n")])
garden = np.pad(garden, 1)


print("Part 1:", part_1(garden))

print("Part 2:", part_2(garden))
