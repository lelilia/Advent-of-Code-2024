def length_digits(number):
    n = number
    counter = 0
    while n > 0:
        n //= 10
        counter += 1
    if counter % 2 == 0:
        return counter // 2
    return False


def setup(file):
    with open(file) as f:
        puzzle = f.read()
    dicts = [{}, {}]
    for p in puzzle.split():
        dicts = insert(dicts, 0, int(p))
    return dicts


def insert(dicts, j, number, count=1):
    if number in dicts[j]:
        dicts[j][number] += count
    else:
        dicts[j][number] = count
    return dicts


def blink(dicts, times):
    for t in range(times):
        i = t % 2
        j = (t + 1) % 2
        for number, count in dicts[i].items():
            if number == 0:
                dicts = insert(dicts, j, 1, count)
            elif split := length_digits(number):
                for new_number in [number // 10**split, number % 10**split]:
                    dicts = insert(dicts, j, new_number, count)
            else:
                dicts = insert(dicts, j, number * 2024, count)
        dicts[i] = {}
    return sum([v for v in dicts[j].values()])


dicts = setup("input11")
print("Part 1:", blink(dicts, 25))

dicts = setup("input11")
print("Part 2:", blink(dicts, 75))
