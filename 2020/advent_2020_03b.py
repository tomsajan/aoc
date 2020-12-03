from aocd import data, submit

def ride(lines, vx, vy):
    dimy = len(lines)
    dimx = len(lines[0])

    x = 0
    y = 0

    counter = 0
    while y < dimy:
        if lines[y][x] == '#':
            counter += 1

        y += vy
        x = (x + vx) % dimx
    return counter
    # submit(counter)


if __name__ == '__main__':
    lines = data.split('\n')

    mu = 1
    for vx, vy in ((1,1), (3,1), (5,1), (7,1), (1,2)):
        mu *= ride(lines, vx, vy)
    print(mu)
    submit(mu)