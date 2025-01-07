from aocd import data, submit
from itertools import pairwise
from collections import namedtuple

import re
data = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

class OutOfMazeException(Exception):
    pass

directions = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3
}
Position = namedtuple('Position', ('x', 'y'))

movements = {
    0: Position(0, -1),
    1: Position(1, 0),
    2: Position(0, 1),
    3: Position(-1, 0)
}


class Coordinate:
    def __init__(self, x, y, field_type):
        self.position = Position(x, y)
        self.type = field_type
        self.visited = False
        self.obstacle = False
        self.last_visited_direction = -1

    def visit(self):
        self.visited = True

    def __str__(self):
        return str(f'{self.type}{'v' if self.visited else ""}')

    def __repr__(self):
        return self.__str__()

class Maze:
    def __init__(self, data):
        self._raw_data = data
        self.maze = {}
        self.x_max = -1
        self.y_max = -1
        self._process_data()
        self.position = Position(-1, -1)
        self.direction = -1


    def __str__(self):
        return str(self.maze)

    def __repr__(self):
        return self.__str__()

    def _print(self):
        for y in range(self.y_max):
            for x in range(self.x_max):
                p = Position(x, y)
                print('0' if self.maze[p].obstacle else self.maze[p].type, end='')
            print()


    def _process_data(self):
        y = 0
        for row in self._raw_data.split():
            x = 0
            for column in list(row):
                self.maze[Position(x, y)] = Coordinate(x, y, column)

                x += 1
            y += 1

        self.x_max = x - 1
        self.y_max = y - 1

        # print(self.x_max, self.y_max)

    def initialize(self):
        for c in self.maze.values():
            if c.type in directions.keys():
                self.position = c.position
                self.direction = directions[c.type]
                self.maze[self.position].visit()
                return


    def rotate(self):
        self.direction = (self.direction + 1) % 4
        # print('rotated to ', movements[self.direction])

    def make_step(self):
        new_position = Position(
            self.position.x + movements[self.direction].x,
            self.position.y + movements[self.direction].y
        )
        # print(f'new test position: {new_position}')
        if new_position.x < 0:
            raise OutOfMazeException()
        if new_position.x > self.x_max:
            raise OutOfMazeException()
        if new_position.y < 0:
            raise OutOfMazeException()
        if new_position.y > self.y_max:
            raise OutOfMazeException()

        return new_position

    def navigate_maze(self):
        loop_counter = 0
        try:
            while True:
                # if counter > 1000:
                #     raise Exception()
                new_position = self.make_step()
                # if self.maze[new_position].type != '.':
                if self.maze[new_position].type == '#':
                    self.rotate()
                    continue

                # test if placing an obstacle would cause a loop
                try:
                    old_direction = self.direction
                    self.rotate()
                    rotated_position = self.make_step()
                    # if we meet already visited field with fake obstacle, we created a loop
                    # if self.maze[rotated_position].visited and self.maze[rotated_position].last_visited_direction == self.direction:
                    if self.maze[rotated_position].visited: #and self.maze[rotated_position].last_visited_direction == self.direction:
                        self.maze[self.position].obstacle = True
                        loop_counter += 1

                except OutOfMazeException:
                    print("inner out of maze")
                    pass
                finally:
                    self.direction = old_direction

                # print(f"moving to {new_position}")
                self.position = new_position
                self.maze[self.position].visit()
                self.maze[self.position].last_visited_direction = self.direction

        except OutOfMazeException:
            print("out of maze :)")
            return loop_counter

if __name__ == '__main__':

    maze = Maze(data)
    maze.initialize()
    loop_counter = maze.navigate_maze()

    # print(maze)


    # for p in (x for x in maze.maze.values() if x.visited):
    #     print(p)

    print(sum(1 for x in maze.maze.values() if x.visited))

    print(loop_counter)
    maze._print()
    #submit(loop_counter)
