import re


def get_game_parameters(game):
    return [int(x) for x in re.findall(r"[+-]?\d+", game)]


def solve(puzzle, offset=0):
    res = 0
    for game in puzzle.split("\n\n"):
        [a_x, a_y, b_x, b_y, p_x, p_y] = get_game_parameters(game)
        p_x += offset
        p_y += offset
        a = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
        b = (p_x - a * a_x) / b_x
        if a % 1 == 0 and b % 1 == 0:
            res += 3 * int(a) + int(b)
    return res


with open("input13") as f:
    puzzle = f.read()

print("Part 1:", solve(puzzle))
print("Part 2:", solve(puzzle, offset=10000000000000))
