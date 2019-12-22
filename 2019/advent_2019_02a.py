from aocd import data, submit
from math import floor


class Intcode:
    def __init__(self, data):
        self.code = list(map(int, data.split(',')))
        self.code[1] = 12
        self.code[2] = 2

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
        for pos in range(0, len(self.code), 4):
            if self.code[pos] == 99:
                print(self.code[0])
                submit(self.code[0])
                break
            func = getattr(self, f'_do_{self.code[pos]}')
            func(pos)

if __name__ == '__main__':
    ic = Intcode(data)
    ic.run()
