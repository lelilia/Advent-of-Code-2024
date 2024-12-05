import numpy as np


def part1(puzzle, i, j):
    found = 0
    for di, dj in [
        [0, 1],  # down
        [0, -1],  # up
        [1, 0],  # right
        [-1, 0],  # left
        [1, 1],  # left top to right buttom
        [1, -1],  # right top to left buttom
        [-1, 1],  # left buttom to right top
        [-1, -1],  # right buttom to left top
    ]:
        if (
            puzzle[i, j]
            + puzzle[i + di, j + dj]
            + puzzle[i + di * 2, j + dj * 2]
            + puzzle[i + di * 3, j + dj * 3]
            == "XMAS"
        ):
            found += 1
    return found


def part2(puzzle, i, j):
    if sorted(
        [
            puzzle[i - 1, j - 1],
            puzzle[i - 1, j + 1],
            puzzle[i + 1, j + 1],
            puzzle[i + 1, j - 1],
        ]
    ) != ["M", "M", "S", "S"]:
        return 0
    if (
        puzzle[i - 1, j - 1] != puzzle[i + 1, j + 1]
        or puzzle[i - 1, j + 1] != puzzle[i + 1, j - 1]
    ):
        return 1
    return 0


if __name__ == "__main__":

    with open("input4") as f:
        puzzle_input = f.read()

    puzzle = [[y for y in x] for x in puzzle_input.split("\n")]

    puzzle = np.array(puzzle)
    puzzle = np.pad(puzzle, 4)

    res = 0

    x = np.where(puzzle == "X")
    for i in range(len(x[0])):
        res += part1(puzzle, x[0][i], x[1][i])
    print("Part 1:", res)

    a = np.where(puzzle == "A")
    res2 = 0
    for i in range(len(a[0])):
        res2 += part2(puzzle, a[0][i], a[1][i])
    print("Part 2:", res2)
