import re


def get_game_parameters(game):
    game_input = re.findall(
        r"Button A: X([+-]\d+), Y([+-]\d+)\nButton B: X([+-]\d+), Y([+-]\d+)\nPrize: X=(\d+), Y=(\d+)",
        game,
    )
    return [int(x) for x in game_input[0]]


def part_1(puzzle):
    res = 0
    for game in puzzle.split("\n\n"):
        game_params = get_game_parameters(game)
        [a_x, a_y, b_x, b_y, p_x, p_y] = game_params
        a = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
        b = (p_x - a * a_x) / b_x
        if a % 1 == 0 and b % 1 == 0 and a <= 100 and b <= 100:
            res += 3 * int(a) + int(b)
    return res


def part_2(puzzle):
    res = 0
    for game in puzzle.split("\n\n"):
        game_params = get_game_parameters(game)
        [a_x, a_y, b_x, b_y, p_x, p_y] = game_params
        p_x += 10000000000000
        p_y += 10000000000000
        a = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
        b = (p_x - a * a_x) / b_x
        if a % 1 == 0 and b % 1 == 0:
            res += 3 * int(a) + int(b)
    return res


with open("input13") as f:
    puzzle = f.read()

print("Part 1:", part_1(puzzle))
print("Part 2:", part_2(puzzle))
