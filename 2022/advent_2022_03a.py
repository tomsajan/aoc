from aocd import data, submit

def get_priority(x):
    if x == x.upper():
        return ord(x) - ord('A') + 27
    else:
        return ord(x) - ord('a') + 1


if __name__ == '__main__':
    itemsum = 0
    for line in data.split('\n'):
        left = line[:len(line)//2]
        right = line[len(line)//2:]
        leftset = set(left)
        rightset = set(right)
        x = set.intersection(leftset, rightset).pop()
        itemsum += get_priority(x)
    submit(itemsum)