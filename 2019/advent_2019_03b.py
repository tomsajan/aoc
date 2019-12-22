from aocd import data, submit
from math import floor
import copy
import sys

class Wire:
    def __init__(self, data):
        self.instructions = data.split(',')
        # self.path = set()
        self.steps = dict()

    def get_points(self):
        return set(self.steps.keys())

    def draw_segment(self, x, y, direction, count, length):
        if direction == 'R':
            for i in range(x + 1, x + 1 + count):
                # self.path.add((i, y))
                point = (i, y)
                length += 1
                if point not in self.steps:
                    self.steps[point] = length

            x = x + count
        if direction == 'L':
            for i in range(x - 1, x - 1 - count, -1):
                # self.path.add((i, y))
                point = (i, y)
                length += 1
                if point not in self.steps:
                    self.steps[point] = length

            x = x - count

        if direction == 'U':
            for j in range(y + 1, y + 1 + count):
                point = (x, j)
                length += 1
                if point not in self.steps:
                    self.steps[point] = length

            y = y + count

        if direction == 'D':
            for j in range(y - 1, y - 1 - count, -1):
                # self.path.add((x, j))
                point = (x, j)
                length += 1
                if point not in self.steps:
                    self.steps[point] = length

            y = y - count

        return x, y, length

    def draw_path(self):
        x = 0
        y = 0
        length = 0
        for i in self.instructions:
            x, y, length = self.draw_segment(x, y, i[0], int(i[1:]), length)

    @staticmethod
    def manha(x, y):
        return abs(x) + abs(y)

    def latency(self, x, y):
        return self.steps[(x, y)]

if __name__ == '__main__':
    splits = data.split()
    # test data
    # splits=['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']
    w1 = Wire(splits[0])
    w2 = Wire(splits[1])

    w1.draw_path()
    w2.draw_path()

    p1 = w1.get_points()
    p2 = w2.get_points()

    z = p1.intersection(p2)

    # submit(min([Wire.manha(*point) for point in z]))
    print(min([Wire.manha(*point) for point in z]))

    # print(min([w1.latency(*point) + w2.latency(*point) for point in z]))
    submit(min([w1.latency(*point) + w2.latency(*point) for point in z]))


