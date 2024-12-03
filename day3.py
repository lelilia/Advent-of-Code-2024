"""
Advent of Code 2024
--- Day 3: Mull It Over ---
"""

import re

def part1(input):
    multipliers = re.findall(r"(?:mul\()(\d{1,3},\d{1,3})(?:\))", input)
    res = 0
    for m in multipliers:
        a, b = [int(x) for x in m.split(",")]
        res += a*b
    return res


def part2(input):
    parts = re.findall(r"(?:^|do\(\))(.+?)(?:$|don\'t\(\))", input)
    res = 0
    for part in parts:
        res += part1(part)
    return res


if __name__ == "__main__":
    with open("input3") as f:
        input = f.read()
    input = input.replace("\n", "")

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))

    assert part1("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") == 161

    assert part2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48
