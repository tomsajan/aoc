from aocd import data, submit

if __name__ == '__main__':
    elfsum = 0
    max = 0
    for n in data.split('\n\n'):
        elfsum = 0
        for m in n.split('\n'):
            elfsum += int(m)
        if elfsum > max:
            max = elfsum
    submit(max)