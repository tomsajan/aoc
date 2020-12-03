from aocd import data, submit


if __name__ == '__main__':
    lines = data.split('\n')
    dimy = len(lines)
    dimx = len(lines[0])
    vx = 3
    vy = 1

    x = 0
    y = 0

    counter = 0
    while y < dimy:
        if lines[y][x] == '#':
            counter += 1

        y += vy
        x = (x + vx) % dimx
    print(counter, x, y)
    submit(counter)