"""
Advent of Code 2024
--- Day 9: Disk Fragmenter ---
"""


class Partition:
    def __init__(self, value, start_index, length) -> None:
        self.value = value
        self.start_index = start_index
        self.length = length

    def __repr__(self) -> str:
        return f"<{self.value}, {self.start_index}, {self.length}>"


def unzip(file):
    data = []
    space = []
    start_index = 0
    for i, length in enumerate(file):
        if i % 2 == 0:
            value = i // 2
            data.append(Partition(value, start_index, length))
        else:
            space.append(Partition(-1, start_index, length))
        start_index += length
    return data, space


def checksum(data):
    res = 0
    for d in data:
        for l in range(d.length):
            res += d.value * (d.start_index + l)
    return res


def defragment_1(data, space):
    for i in range(len(data) - 1, -1, -1):
        for j in range(len(space)):
            if space[j].length == 0:
                continue
            if space[j].length > data[i].length:
                data[i].start_index = space[j].start_index
                space[j].start_index += data[i].length
                space[j].length -= data[i].length
            if space[j].length < data[i].length:
                data

                space[j].length = 0


def defragment_2(data, space):
    for i in range(len(data) - 1, -1, -1):
        for j in range(len(space)):
            if (
                data[i].length <= space[j].length
                and data[i].start_index > space[j].start_index
            ):
                data[i].start_index = space[j].start_index
                space[j].start_index += data[i].length
                space[j].length -= data[i].length
    return data


def unzip_file(file):
    res = []
    id = 0
    for i in range(len(file)):
        value = file[i]
        if i % 2 == 0:
            res.extend([id] * value)
            id += 1
        else:
            res.extend([-1] * value)
    return res


def rearrange_file(file):
    new_file = []
    while file:

        x = file.pop(0)
        if x != -1:
            new_file.append(x)
        else:
            while file and x == -1:
                x = file.pop()
            if x != -1:
                new_file.append(x)
    return new_file


def calculate_sum(file):
    res = 0
    for i in range(len(file)):
        res += file[i] * i
    return res


def part_2(files):
    data, space = unzip(files)
    data = defragment_2(data, space)
    return checksum(data)


if __name__ == "__main__":
    with open("testinput9") as f:
        puzzle = f.read()

    puzzle = [int(x) for x in puzzle]

    unzipped = unzip_file(puzzle)

    file = rearrange_file(unzipped)

    print("Part 1:", calculate_sum(file))

    print("Part 2:", part_2(puzzle))
