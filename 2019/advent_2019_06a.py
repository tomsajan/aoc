from aocd import data, submit
from collections import defaultdict

class Planet:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = set()
        self.dist = 0

    def get_dist(self):
        return self.dist

    def set_dist(self, dist):
        self.dist = dist

    def get_parent_dist(self):
        if self.parent is None:
            return 0
        return self.parent.get_dist()

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.add(child)

    def __str__(self):
        return f'Planet {self.name}'


if __name__ == '__main__':
#     data = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L"""

    relations = defaultdict(set)
    for relation in data.split():
        a, b = relation.split(')')
        relations[a].add(b)
    print(relations)
    COM = Planet('COM')
    open = set([COM])

    while len(open) > 0:
        p = open.pop()
        for r in relations[p.name]:
            ch = Planet(r)
            ch.set_parent(p)
            ch.set_dist(p.get_dist() + 1)
            print(f'planet {ch.name} dist {ch.get_dist()}')
            p.add_child(ch)
            open.add(ch)

    # open.add(COM)
    # while len(open) > 0:
    #     planet = open.pop()
    #     planet.set_dist(planet.get_dist() + 1)
    #     open |= planet.children

    open.add(COM)
    sum = 0
    while len(open) > 0:
        planet = open.pop()
        sum += planet.get_dist()
        open |= planet.children
    print(sum)
    submit(sum)

