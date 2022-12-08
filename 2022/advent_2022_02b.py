from aocd import data, submit

ROCK = 0
PAPER = 1
SCISSORS = 2


T = {
    'A': ROCK,
    'X': ROCK,
    'B': PAPER,
    'Y': PAPER,
    'C': SCISSORS,
    'Z': SCISSORS,
}

M = {
    ROCK: 'X',
    PAPER: 'Y',
    SCISSORS: 'Z',
}


def match(opponent, myself):
    score = 0
    score += T[myself] + 1
    if T[opponent] == T[myself]:
        score += 3
    elif (T[opponent] + 1) % 3 == T[myself]:
        score += 6
    return score


def get_move(opponent, instruction):
    if instruction == 'X':
        return M[(T[opponent] - 1) % 3]
    if instruction == 'Y':
        return opponent
    if instruction == 'Z':
        return M[(T[opponent] + 1) % 3]


if __name__ == '__main__':
    total_score = 0
    for n in data.split('\n'):
        o, m = n.split()
        score = match(o, get_move(o, m))
        total_score += score
    submit(total_score)
