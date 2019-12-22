from aocd import data, submit
from math import floor
import copy
import sys


class Intcode:
    def __init__(self, data):
        self.init_code = list(map(int, data.split(',')))
        self.code = []
        self.reset()

    def set_noun(self, noun):
        self.code[1] = noun

    def set_verb(self, verb):
        self.code[2] = verb

    def reset(self):
        self.code = copy.deepcopy(self.init_code)

    def _do_1(self, pos):
        pos1 = self.code[pos+1]
        pos2 = self.code[pos+2]
        pos3 = self.code[pos+3]
        self.code[pos3] = self.code[pos1] + self.code[pos2]

    def _do_2(self, pos):
        pos1 = self.code[pos+1]
        pos2 = self.code[pos+2]
        pos3 = self.code[pos+3]
        self.code[pos3] = self.code[pos1] * self.code[pos2]


    def run(self):
        target = 19690720
        for noun in range(0, 99+1):
            for verb in range(0, 99+1):
                self.reset()
                self.set_noun(noun)
                self.set_verb(verb)

                for pos in range(0, len(self.code), 4):
                    if self.code[pos] == 99:
                        if target == self.code[0]:
                            print(100*noun + verb)
                            submit(100 * noun + verb)
                            sys.exit(0)
                        break
                    func = getattr(self, f'_do_{self.code[pos]}')
                    func(pos)

if __name__ == '__main__':
    ic = Intcode(data)
    ic.run()
