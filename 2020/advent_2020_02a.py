from aocd import data, submit
from collections import Counter

def parse_line(line):
    line = line.split(' ')
    pw = line[-1]
    low, high = line[0].split('-')
    ch = line[1][0]

    return int(low), int(high), ch, pw

def verify_pw(low, high, ch, pw):
    count = Counter(pw)
    if low <= count[ch] <= high:
        return 1
    else:
        return 0

if __name__ == '__main__':
    lines = data.split('\n')
    counter = 0

    for line in lines:
        counter += verify_pw(*parse_line(line))
    print(counter)
    submit(counter)

