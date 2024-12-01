from aocd import data, submit

from collections import Counter
from itertools import cycle, pairwise


#data = '''0 3 6 9 12 15
#1 3 6 10 15 21
#10 13 16 21 30 45'''

class Series:
    def __init__(self, series):
        if isinstance(series, str):
            series = series.split()
        self.data = [int(x) for x in series]
        self.parent = None
        self.child = None

        if not self.is_all_zero():
            child = self.make_child()
            self.set_child(child)
            child.set_parent(self)
        #print(self)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

    def set_parent(self, parent):
        self.parent = parent

    def set_child(self, child):
        self.child = child

    def is_all_zero(self):
        return all(x == 0 for x in self.data)

    def make_child(self):
        return Series([j-i for i, j in pairwise(self.data)])
        
    def make_prediction(self):
        if self.is_all_zero():
            self.data.insert(0, 0)
        else:
            self.child.make_prediction()
            self.data.insert(0, self.data[0]-self.child.data[0])


if __name__ == '__main__':
    lines = data.split('\n')
    series = [Series(s) for s in lines]
    for serie in series:
        serie.make_prediction()
    print(sum(s.data[0]  for s in series))
    submit(sum(s.data[0]  for s in series))



