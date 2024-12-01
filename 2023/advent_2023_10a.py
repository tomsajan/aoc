from aocd import data, submit

from collections import Counter
from itertools import cycle, pairwise, product


#data = '''0 3 6 9 12 15
#1 3 6 10 15 21
#10 13 16 21 30 45'''

data = '''.....
.S-7.
.|.|.
.L-J.
.....'''

M = {
  ('U', '|'): 'U',
  ('D', '|'): 'D',
  ('U', 'F'): 'R',
  ('U', '7'): 'L',
  ('D', 'L'): 'R',
  ('D', 'J'): 'L',
  ('L', 'F'): 'D',
  ('L', 'L'): 'R',
  ('L', '-'): 'L',
  ('R', '-'): 'R',
  ('R', '7'): 'D',
  ('R', 'J'): 'U',
}

class Field:
    def __init__(self, field):
        self.field = field
        self.dist = 0

    def __repr__(self):
        return self.field

class Maze:
    def __init__(self, lines):
        self.maze = {}
        self.directions = []
        for x, y in product(list(range(len(lines[0]))), list(range(len(lines)))):
            self.maze[x, y] = None

        for y, line in enumerate(lines):
            for x, value in enumerate(line):
                if value == 'S':
                    self.start = (x, y)
                self.maze[x, y] = Field(value)
        self.positions = [self.start, self.start]
    
    def __repr__(self): 
        return str(self.maze)


    def get_init_directions(self):   
        # no checking if S is at border
        if self.maze[self.start[0]-1, self.start[1]].field in {'-', 'L', 'F'}:
            self.directions.append('L')
        if self.maze[self.start[0]+1, self.start[1]].field in {'-', '7', 'J'}:
            print('juhuu')
            self.directions.append('R')
        if self.maze[self.start[0], self.start[1]-1].field in {'|', 'F', '7'}:
            self.directions.append('U')
        if self.maze[self.start[0], self.start[1]+1].field in {'|', 'L', 'J'}:
            print('juhuu')
            self.directions.append('D')

    
    def search(self):
        dist = self.maze[self.start].dist
        for _ in range(10):
            dist += 1
            print('dist', dist)
            print(self.directions, self.positions)
            for d in range(len(self.directions)):
                nextd = M[self.directions[d], self.maze[self.positions[d]].field]
                self.directions[d] = nextd
                if nextd == 'U':
                    self.positions[d] = (self.positions[d][0]-1, self.positions[d][1])
                if nextd == 'D':
                    self.positions[d] = (self.positions[d][0]+1, self.positions[d][1])
                if nextd == 'L':
                    self.positions[d] = (self.positions[d][0], self.positions[d][1]-1)
                if nextd == 'R':
                    self.positions[d] = (self.positions[d][0], self.positions[d][1]+1)

                if self.positions[d].dist > 0:
                    print('FOUND')
                    print(self.positions[d].dist)
                    return self.positions[d].dist
                self.positions[d].dist = dist



if __name__ == '__main__':
    lines = data.split('\n')
    m = Maze(lines)
    m.get_init_directions()
    print('start', m.start)
    print(m)

    m.search()

    print(len(lines))
    print(len(lines[0]))

