from aocd import data, submit
#
# data = '''    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2'''


state = {}


def do_move(source, target, count):
    state[target].extend(state[source][-count:])
    del state[source][-count:]


if __name__ == '__main__':
    # parse initial state
    initial_state, moves = data.split('\n\n')
    lines = initial_state.split('\n')
    zlines = zip(*lines)
    for line in zlines:
        rline = list(line)
        rline.reverse()
        if rline[0] == ' ':
            continue
        fline = [i for i in rline if i != ' ']
        state[fline[0]] = fline[1:]

    for move in moves.split('\n'):
        splits = move.split(' ')
        do_move(splits[3], splits[5], int(splits[1]))

    result = []
    for key in sorted(state.keys()):
        result.append(state[key][-1])
    result = ''.join(result)
    print(result)

    # print(counter)
    submit(result)
    # submit(itemsum)