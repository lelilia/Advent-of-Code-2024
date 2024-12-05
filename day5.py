class Page:
    def __init__(self, name) -> None:
        self.name = name
        self.after = []
        self.prev = []

    def __repr__(self) -> str:
        return str(self.name)

    def add_later_page(self, later):
        self.after.append(later)

    def add_prev_page(self, prev):
        self.prev.append(prev)

    def is_bigger(self, other):
        if other in self.after:
            return False
        elif other in self.prev:
            return True


def check_update(update, pages):
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if pages[update[j]] in pages[update[i]].prev:
                return False
    return True


def reorder_update(update, pages):
    curr = update.pop()
    ordered_update = [curr]
    while len(update) > 0:
        curr = update.pop()

        for i in range(len(ordered_update)):
            if pages[ordered_update[i]].is_bigger(pages[curr]):
                ordered_update.insert(i, curr)
                break
        else:
            ordered_update.append(curr)

    return ordered_update[len(ordered_update) // 2]


if __name__ == "__main__":

    with open("input5") as f:
        puzzle_input = f.read()

    orders, updates = puzzle_input.split("\n\n")

    pages = {}
    for order in orders.split("\n"):
        prev, later = [int(x) for x in order.split("|")]

        if prev not in pages:
            pages[prev] = Page(prev)

        if later not in pages:
            pages[later] = Page(later)

        pages[prev].add_later_page(pages[later])
        pages[later].add_prev_page(pages[prev])

    res = 0
    res_2 = 0

    for update in updates.split("\n"):
        update = [int(x) for x in update.split(",")]

        if check_update(update, pages):
            res += update[len(update) // 2]
        else:
            res_2 += reorder_update(update, pages)
    print("Part 1:", res)
    print("Part 2:", res_2)
