"""
Advent of Code 2024
--- Day 1: Historian Hysteria ---
"""


def parse_list(file):
    with open(file, "r") as f:
        input = f.readlines()
    list1 = []
    list2 = []

    for line in input:
        x1, x2 = line.split()
        list1.append(int(x1))
        list2.append(int(x2))

    list1.sort()
    list2.sort()
    return list1, list2


def part_1(list1, list2):

    diff = 0
    for i in range(len(list1)):
        diff += abs(list1[i] - list2[i])
    return diff


def part_2(list1, list2):
    sim = 0
    for i in range(len(list1)):
        sim += list2.count(list1[i]) * list1[i]
    return sim


if __name__ == "__main__":
    list1, list2 = parse_list("input1")

    print("Part 1:", part_1(list1, list2))
    print("Part 2:", part_2(list1, list2))
