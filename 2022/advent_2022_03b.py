from aocd import data, submit
# from itertools import zip
def get_priority(x):
    if x == x.upper():
        return ord(x) - ord('A') + 27
    else:
        return ord(x) - ord('a') + 1


if __name__ == '__main__':
    itemsum = 0
    for a, b, c in zip(*[iter(data.split('\n'))] * 3):
        aset = set(a)
        bset = set(b)
        cset = set(c)
        x = set.intersection(aset, bset, cset).pop()
        itemsum += get_priority(x)
    submit(itemsum)