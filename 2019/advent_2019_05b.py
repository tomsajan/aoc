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

    def interprete_param(self, param, mode):
        mode = mode[-param] if len(mode) >= param else '0'
        if mode == '0':
            return self.code[self.pos + param]
        if mode == '1':
            return self.pos + param


    def _do_1(self, mode):

        par1 = self.interprete_param(1, mode)
        par2 = self.interprete_param(2, mode)
        par3 = self.interprete_param(3, mode)

        self.code[par3] = self.code[par1] + self.code[par2]
        self.pos += 4

    def _do_2(self, mode):
        par1 = self.interprete_param(1, mode)
        par2 = self.interprete_param(2, mode)
        par3 = self.interprete_param(3, mode)

        self.code[par3] = self.code[par1] * self.code[par2]
        self.pos += 4

    def _do_3(self, mode):
        par1 = self.interprete_param(1, mode)
        self.code[par1] = self.input
        self.pos += 2

    def _do_4(self, mode):
        par1 = self.interprete_param(1, mode)
        self.output = self.code[par1]
        self.pos += 2
        print('Output', self.output)

    def _do_5(self, mode):
        par1 = self.interprete_param(1, mode)
        par2 = self.interprete_param(2, mode)

        if self.code[par1] != 0:
            self.pos = self.code[par2]
        else:
            self.pos += 3

    def _do_6(self, mode):
        par1 = self.interprete_param(1, mode)
        par2 = self.interprete_param(2, mode)

        if self.code[par1] == 0:
            self.pos = self.code[par2]
        else:
            self.pos += 3

    def _do_7(self, mode):
        par1 = self.interprete_param(1, mode)
        par2 = self.interprete_param(2, mode)
        par3 = self.interprete_param(3, mode)

        if self.code[par1] < self.code[par2]:
            self.code[par3] = 1
        else:
            self.code[par3] = 0

        self.pos += 4

    def _do_8(self, mode):
        par1 = self.interprete_param(1, mode)
        par2 = self.interprete_param(2, mode)
        par3 = self.interprete_param(3, mode)

        if self.code[par1] == self.code[par2]:
            self.code[par3] = 1
        else:
            self.code[par3] = 0
        self.pos += 4

    def _do_99(self, mode):
        print('Exit', self.code[0])
        submit(ic.output)
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
        self.set_input(5)

        while True:
            opcode = self.code[self.pos]
            mode, op = self.parse_opcode(opcode)

            func = getattr(self, f'_do_{op}')
            func(mode)


if __name__ == '__main__':
    # data = '3,225,1,225,6,6,1100,1,238,225,104,0,1101,82,10,225,101,94,44,224,101,-165,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1102,35,77,225,1102,28,71,225,1102,16,36,225,102,51,196,224,101,-3468,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1001,48,21,224,101,-57,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,2,188,40,224,1001,224,-5390,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,9,32,224,101,-41,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1102,66,70,225,1002,191,28,224,101,-868,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1,14,140,224,101,-80,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1102,79,70,225,1101,31,65,225,1101,11,68,225,1102,20,32,224,101,-640,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,226,224,1002,223,2,223,1006,224,329,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,359,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,374,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,7,677,226,224,1002,223,2,223,1006,224,404,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,419,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,7,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,464,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,479,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,509,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,554,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,629,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,644,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,659,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226'
    # data = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,9,19,23,2,23,13,27,1,27,9,31,2,31,6,35,1,5,35,39,1,10,39,43,2,43,6,47,1,10,47,51,2,6,51,55,1,5,55,59,1,59,9,63,1,13,63,67,2,6,67,71,1,5,71,75,2,6,75,79,2,79,6,83,1,13,83,87,1,9,87,91,1,9,91,95,1,5,95,99,1,5,99,103,2,13,103,107,1,6,107,111,1,9,111,115,2,6,115,119,1,13,119,123,1,123,6,127,1,127,5,131,2,10,131,135,2,135,10,139,1,13,139,143,1,10,143,147,1,2,147,151,1,6,151,0,99,2,14,0,0'
    # data = '1,0,0,0,99'
    # data = '1101,100,-1,4,0'
    # data = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'
    # data = '3,9,8,9,10,9,4,9,99,-1,8'
    ic = Intcode(data)
    ic.run()
