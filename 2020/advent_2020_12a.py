from aocd import submit
from aocd import data
import numpy as np
from collections import Counter

import re

# data="""F10
# N3
# F7
# R90
# F11"""


DIR = {
    0: 'E',
    90: 'S',
    180: 'W',
    270: 'N'
}

class Nav:
    def __init__(self, lines):
        self.dir = 0
        self.x = 0
        self.y = 0
        self.instructions = []
        self.parse_instructions(lines)

    def parse_instructions(self, lines):
        for instruction in lines:
            self.instructions.append((instruction[0], int(instruction[1:])))


    def _do_R(self, value):
        self.dir = (self.dir + value) % 360

    def _do_L(self, value):
        self.dir = (self.dir - value) % 360

    def _do_F(self, value):
        direction = DIR[self.dir]
        func = getattr(self, f'_do_{direction}')
        func(value)

    def _do_N(self, value):
        self.y += value

    def _do_S(self, value):
        self.y -= value

    def _do_E(self, value):
        self.x += value

    def _do_W(self, value):
        self.x -= value

    def run(self):
        for instruction, value in self.instructions:
            func = getattr(self, f'_do_{instruction}')
            func(value)

    def get_manhattan(self):
        return abs(self.x) + abs(self.y)

if __name__ == '__main__':
    lines = data.split('\n')
    n = Nav(lines)
    n.run()
    md = n.get_manhattan()
    print(md, n.x, n.y)
    submit(md)
