from aocd import data, submit
from math import floor

if __name__ == '__main__':
    elfsum = 0
    elfset = set()
    for n in data.strip().split('\n\n'):
        elfsum = 0
        for m in n.split('\n'):
            elfsum += int(m)
        elfset.add(elfsum)

    elfset = list(elfset)
    elfset.sort(reverse=True)
    submit(sum(elfset[0:3]))
