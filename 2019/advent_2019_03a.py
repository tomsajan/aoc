from aocd import data, submit
from math import floor
import copy
import sys

class Wire:
    def __init__(self, data):
        self.instructions = data.split(',')
        self.path = set()

    def draw_segment(self, x, y, direction, count):
        if direction == 'R':
            for i in range(x + 1, x + 1 + count):
                self.path.add((i, y))
            x = x + count
        if direction == 'L':
            for i in range(x - 1, x - 1 - count, -1):
                self.path.add((i, y))
            x = x - count

        if direction == 'U':
            for j in range(y + 1, y + 1 + count):
                self.path.add((x, j))
            y = y + count

        if direction == 'D':
            for j in range(y - 1, y - 1 - count, -1):
                self.path.add((x, j))
            y = y - count

        return x, y

    def draw_path(self):
        x = 0
        y = 0

        for i in self.instructions:
            x, y = self.draw_segment(x, y, i[0], int(i[1:]))

    @staticmethod
    def manha(x, y):
        return abs(x) + abs(y)

if __name__ == '__main__':
    splits = data.split()
    # test data
    # splits=['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']
    w1 = Wire(splits[0])
    w2 = Wire(splits[1])

    w1.draw_path()
    w2.draw_path()

    z = w1.path.intersection(w2.path)

    submit(min([Wire.manha(*point) for point in z]))
