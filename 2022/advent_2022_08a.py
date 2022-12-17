from aocd import data, submit
# data = '''30373
# 25512
# 65332
# 33549
# 35390'''


if __name__ == '__main__':
    trees = data.split('\n')
    counter = 0

    # assuming square... it is actually
    dim = len(trees)

    for i in range(dim):
        for j in range(dim):
            # on the border
            if i in (0, dim - 1) or j in (0, dim - 1):
                counter += 1
                continue

            cycle_left = False
            for x in range(i-1, -1, -1):
                if trees[x][j] >= trees[i][j]:
                    cycle_left = True
                    break
            # this means we scrolled to the border, thus visible
            if not cycle_left:
                counter +=1
                continue

            cycle_left = False
            for x in range(i + 1, dim):
                if trees[x][j] >= trees[i][j]:
                    cycle_left = True
                    break
            # this means we scrolled to the border, thus visible
            if not cycle_left:
                counter += 1
                continue

            cycle_left = False
            for y in range(j - 1, -1, -1):
                if trees[i][y] >= trees[i][j]:
                    cycle_left = True
                    break
            # this means we scrolled to the border, thus visible
            if not cycle_left:
                counter += 1
                continue

            cycle_left = False
            for y in range(j + 1, dim):
                if trees[i][y] >= trees[i][j]:
                    cycle_left = True
                    break
            # this means we scrolled to the border, thus visible
            if not cycle_left:
                counter += 1
                continue




    print(counter)
    submit(counter)