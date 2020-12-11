from aocd import submit
from aocd import data

import re
import copy

# data="""nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# nop -4
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

        try:
            while self.instructions[self.pos]['counter'] == 0:
                func = getattr(self, f'_do_{self.instructions[self.pos]["opname"]}')
                self.instructions[self.pos]['counter'] += 1
                func()
        except IndexError:
            loop = False

        else:
            loop = True

        return self.accumulator, loop


if __name__ == '__main__':

    lines = data.split('\n')
    instructions_orig = [parse_instructions(op) for op in lines]

    loop = True
    i = 0
    while loop:
        instructions = copy.deepcopy(instructions_orig)
        if instructions[i]['opname'] == 'nop':
            instructions[i]['opname'] = 'jmp'
            acc, loop = Opmachine(instructions).run()
            instructions[i]['opname'] = 'nop'
        elif instructions[i]['opname'] == 'jmp':
            instructions[i]['opname'] = 'nop'
            acc, loop = Opmachine(instructions).run()
            instructions[i]['opname'] = 'jmp'

        i += 1
    print(acc)




    # print(len(found))
    submit(acc)
