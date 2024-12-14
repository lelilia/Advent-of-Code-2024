"""
Advent of Code 2024
"""

import numpy as np
import re

TIMES = 100
X = 101
Y = 103

# X = 11
# Y = 7


class Robot:
    def __init__(self, p_x, p_y, v_x, v_y) -> None:
        self.p_x = p_x
        self.p_y = p_y
        self.v_x = v_x
        self.v_y = v_y

    def __repr__(self) -> np.str:
        return f"{self.p_x}, {self.p_y}, {self.v_x}, {self.p_y}"

    def move(self):
        self.p_x = (self.p_x + self.v_x) % X
        self.p_y = (self.p_y + self.v_y) % Y


def print_robots(robots):
    floor = np.array([["." for x in range(Y)] for y in range(X)])
    for r in robots:
        floor[r.p_x, r.p_y] = "X"
    p_floor = ""
    for row in floor:
        p_floor += "".join(row) + "\n"
    return p_floor


with open("input14") as f:
    puzzle_input = f.read()

robots = []

for robot in puzzle_input.split("\n"):

    robots.append(Robot(*[int(r) for r in re.findall(r"[+-]?\d+", robot)]))

for t in range(TIMES):

    for i in range(len(robots)):
        robots[i].move()
    if t % X == 27 or t % Y == 85:
        with open("test_day14_output", "a") as f:
            f.write(str(t) + "\n" + print_robots(robots) + "\n\n")


q_1 = q_2 = q_3 = q_4 = 0

for r in robots:
    if r.p_x < X // 2 and r.p_y < Y // 2:
        q_1 += 1
    elif (X + 1) // 2 <= r.p_x and r.p_y < Y // 2:
        q_2 += 1
    elif r.p_x < X // 2 and (Y + 1) // 2 <= r.p_y:
        q_3 += 1
    elif (X + 1) // 2 <= r.p_x and (Y + 1) // 2 <= r.p_y:
        q_4 += 1


print("Part 1:", q_1 * q_2 * q_3 * q_4)

print("Part 2:")
