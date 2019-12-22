from aocd import data, submit
from math import floor
import copy
import sys


class Intcode:
    def __init__(self, data):
        self.init_code = list(map(int, data.split(',')))
        self.code = []
        self.pos = 0
        self.input = 0
        self.output = 0
        self.reset()

    def set_input(self, input):
        self.input = input

    def set_noun(self, noun):
        self.code[1] = noun

    def set_verb(self, verb):
        self.code[2] = verb

    def reset(self):
        self.code = copy.deepcopy(self.init_code)
        self.pos = 0

    def interprete_param(self, pos, mode):
        if mode == '0':
            return self.code[pos]
        if mode == '1':
            return pos


    def _do_1(self, mode):

        par1 = self.interprete_param(self.pos + 1, mode[-1] if len(mode) >= 1 else '0')
        par2 = self.interprete_param(self.pos + 2, mode[-2] if len(mode) >= 2 else '0')
        par3 = self.interprete_param(self.pos + 3, mode[-3] if len(mode) >= 3 else '0')

        self.code[par3] = self.code[par1] + self.code[par2]
        self.pos += 4

    def _do_2(self, mode):
        par1 = self.interprete_param(self.pos + 1, mode[-1] if len(mode) >= 1 else '0')
        par2 = self.interprete_param(self.pos + 2, mode[-2] if len(mode) >= 2 else '0')
        par3 = self.interprete_param(self.pos + 3, mode[-3] if len(mode) >= 3 else '0')

        self.code[par3] = self.code[par1] * self.code[par2]
        self.pos += 4

    def _do_3(self, mode):
        par1 = self.interprete_param(self.pos + 1, mode[-1] if len(mode) >= 1 else '0')
        self.code[par1] = self.input
        self.pos += 2

    def _do_4(self, mode):
        par1 = self.interprete_param(self.pos + 1, mode[-1] if len(mode) >= 1 else '0')
        self.output = self.code[par1]
        self.pos += 2
        print('Output', self.output)

    def _do_99(self, mode):
        print('Exit', self.code[0])
        # submit(ic.output)
        sys.exit(0)

    @staticmethod
    def parse_opcode(code):
        code = str(code)
        mode = code[:-2]
        op = code[-2:]
        return mode, int(op)


    def run(self):
        self.reset()
        # self.set_noun(noun)
        # self.set_verb(verb)
        # self.set_noun(12)
        # self.set_verb(2)
        self.set_input(1)

        while True:
            opcode = self.code[self.pos]
            mode, op = self.parse_opcode(opcode)

            func = getattr(self, f'_do_{op}')
            func(mode)


if __name__ == '__main__':
    print(data)
    sys.exit(0)
    # data = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,9,19,23,2,23,13,27,1,27,9,31,2,31,6,35,1,5,35,39,1,10,39,43,2,43,6,47,1,10,47,51,2,6,51,55,1,5,55,59,1,59,9,63,1,13,63,67,2,6,67,71,1,5,71,75,2,6,75,79,2,79,6,83,1,13,83,87,1,9,87,91,1,9,91,95,1,5,95,99,1,5,99,103,2,13,103,107,1,6,107,111,1,9,111,115,2,6,115,119,1,13,119,123,1,123,6,127,1,127,5,131,2,10,131,135,2,135,10,139,1,13,139,143,1,10,143,147,1,2,147,151,1,6,151,0,99,2,14,0,0'
    # data = '1,0,0,0,99'
    # data = '1101,100,-1,4,0'
    ic = Intcode(data)
    ic.run()

