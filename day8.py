"""
Advent of Code 2024
Day 8
"""

import numpy as np


def part_1(puzzle_x, puzzle_y, antennas):
    nodes = {}
    for antenna_positions in antennas.values():

        for i in range(len(antenna_positions) - 1):
            for j in range(i + 1, len(antenna_positions)):
                pos_1 = antenna_positions[i]
                pos_2 = antenna_positions[j]

                dx = pos_1[0] - pos_2[0]
                dy = pos_1[1] - pos_2[1]

                pos_0 = (pos_1[0] + dx, pos_1[1] + dy)
                pos_3 = (pos_2[0] - dx, pos_2[1] - dy)

                if 0 <= pos_0[0] < puzzle_x and 0 <= pos_0[1] < puzzle_y:
                    nodes[pos_0] = True
                if 0 <= pos_3[0] < puzzle_x and 0 <= pos_3[1] < puzzle_y:
                    nodes[pos_3] = True

    return len(nodes)


def part_2(puzzle_x, puzzle_y, antennas):
    nodes = {}
    for antenna_positions in antennas.values():
        for i in range(len(antenna_positions) - 1):
            for j in range(i + 1, len(antenna_positions)):
                pos_1 = antenna_positions[i]
                pos_2 = antenna_positions[j]

                dx = pos_1[0] - pos_2[0]
                dy = pos_1[1] - pos_2[1]

                x = pos_1[0]
                y = pos_1[1]
                while 0 <= x < puzzle_x and 0 <= y < puzzle_y:
                    nodes[(x, y)] = True
                    x += dx
                    y += dy
                x = pos_1[0]
                y = pos_1[1]
                while 0 <= x < puzzle_x and 0 <= y < puzzle_y:
                    nodes[(x, y)] = True
                    x -= dx
                    y -= dy

    return len(nodes)


with open("input8") as f:
    puzzle = f.read()
    puzzle = [[y for y in x] for x in puzzle.split("\n")]
    puzzle = np.array(puzzle)


antennas = {}
nodes = {}

puzzle_x, puzzle_y = puzzle.shape
# print(puzzle_x, puzzle_y)

for antenna_type in np.unique(puzzle):
    if antenna_type == ".":
        continue
    locations = np.where(puzzle == antenna_type)

    antenna_positions = list(zip(locations[0], locations[1]))
    antennas[antenna_type] = antenna_positions


print("Part 1:", part_1(puzzle_x, puzzle_y, antennas))
print("Part 2:", part_2(puzzle_x, puzzle_y, antennas))
