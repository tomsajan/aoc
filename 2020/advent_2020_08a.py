from aocd import submit
from aocd import data

import re

# data="""nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""

def parse_instructions(line):
    opname, val = line.strip().split(' ')
    return {
        'opname': opname,
        'val': int(val),
        'counter': 0
    }


class Opmachine:
    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator = 0
        self.pos = 0

    def _do_nop(self):
        self.pos += 1

    def _do_acc(self):
        self.accumulator += self.instructions[self.pos]['val']
        self.pos += 1

    def _do_jmp(self):
        self.pos += self.instructions[self.pos]['val']

    def run(self):

        while self.instructions[self.pos]['counter'] == 0:
            func = getattr(self, f'_do_{self.instructions[self.pos]["opname"]}')
            self.instructions[self.pos]['counter'] += 1
            func()

        print(self.accumulator)
        # submit(self.accumulator)


if __name__ == '__main__':

    lines = data.split('\n')
    instructions = [parse_instructions(op) for op in lines]
    om = Opmachine(instructions)
    om.run()


    # print(len(found))
    # submit(len(found))
