import re

class Program:
    def __init__(self, program, a=0, b=0, c=0, is_part_2=False) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.pointer = 0
        self.program = program
        self.output = []
        self.combo = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.a,
            5: self.b,
            6: self.c,
        }
        self.is_part_2 = is_part_2

    def get_combo(self, number):
        if number < 4:
            return number
        elif number == 4:
            return self.a
        elif number == 5:
            return self.b
        elif number == 6:
            return self.c


    def run(self):
        while self.pointer < len(self.program):
            operand = self.program[self.pointer]
            # print(f"{operand}, ")
            # print(f"{operand}, {self.program[self.pointer + 1]}, {self.get_combo(self.program[self.pointer + 1])}, \nA: {self.a}, \tB: {self.b}, \tC: {self.c}, \tout: {self.output}\n")
            if operand == 0:
                self.adv()
            elif operand == 1:
                self.bxl()
            elif operand == 2:
                self.bst()
            elif operand == 3:
                self.jnz()
            elif operand == 4:
                self.bxc()
            elif operand == 5:
                if self.is_part_2:
                    return self.get_combo(self.program[self.pointer + 1]) % 8
                self.out()
            elif operand == 6:
                self.bdv()
            elif operand == 7:
                self.cdv()


    def adv(self):
        self.a = self.a // (2 ** self.get_combo(self.program[self.pointer + 1]))
        self.pointer += 2

    def bxl(self):
        self.b = self.b ^ self.program[self.pointer + 1]
        self.pointer += 2

    def bst(self):
        self.b = self.get_combo(self.program[self.pointer + 1]) % 8
        self.pointer += 2

    def jnz(self):
        if self.a == 0:
            self.pointer += 2
            return
        self.pointer = self.program[self.pointer + 1]

    def bxc(self):
        self.b = self.b ^ self.c
        self.pointer += 2

    def out(self):
        value = self.get_combo(self.program[self.pointer + 1]) % 8
        self.output.append(value)
        self.pointer += 2

    def bdv(self):
        self.b = self.a // (2 ** self.get_combo(self.program[self.pointer + 1]))
        self.pointer += 2

    def cdv(self):
        self.c = self.a // (2 ** self.get_combo(self.program[self.pointer + 1]))
        self.pointer += 2

with open("input17") as f:
    puzzle_input = f.read()

setup, program = puzzle_input.split("\n\n")

a, b, c = [int(x) for x in re.findall(r"\d+", setup)]

program = [int(x) for x in program.replace("Program: ", "").split(",")]

p = Program(program=program, a=a, b=b, c=c)
p.run()
print("Part 1:", ",".join([str(x) for x in p.output]))

q = program.copy()
res = 0
while q:
    curr = q.pop()

    for i in range(8):

        p = Program(program, a=res*8+i, is_part_2=True)
        f = p.run()
        if f == curr:
            res = res * 8 + i
            break

print("Part 2:", res)





# p = Program(program=[2,6], c=9)
# p.run()
# assert p.b == 1

# p = Program(program=[5,0,5,1,5,4], a=10)
# p.run()
# assert p.output == [0,1,2]

# p = Program(program=[0,2], a=16)
# p.run()
# assert p.a == 4, f"expected 4 got {p.a}"

# p = Program(program=[0,1,5,4,3,0], a=2024)
# p.run()
# assert p.output == [4,2,5,6,7,7,7,7,3,1,0] and p.a == 0, f"{p.output}, {p.a}"

# p = Program(program=[1,7], b=29)
# p.run()
# assert p.b == 26

# p = Program(program=[4,0], b=2024, c=43690)
# p.run()
# assert p.b == 44354

# p = Program(program=[0,1,5,4,3,0], a=729)
# p.run()
# assert p.output == [4,6,3,5,6,3,5,2,1,0]