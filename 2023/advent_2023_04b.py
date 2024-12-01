from aocd import data, submit
#from collections import namedtuple


#data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
#Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
#Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
#Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
#Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''


scores = 0

def parse_line(line):
    card, line = line.split(':')
    card = int(card.split()[1])
    splits = line.split('|')
    winning = {int(num.strip()) for num in splits[0].split()}
    yours = {int(num.strip()) for num in splits[1].split()}
    return card, winning, yours

def set_score(points, index, depth=''):
    global scores
    if 0 <= index < len(points):
        #print(depth, 'Card ', index+1, 'points ', points[index])
        scores += 1
    else:
        return
    if points[index] == 0:
        return 
    for i in range(index+1, index+points[index]+1):
        set_score(points, i, depth + '  ')


if __name__ == '__main__':
    cards = [parse_line(line) for line in data.splitlines()]
    points = [len(card[1].intersection(card[2])) for card in cards]
    print(points)
    for i in range(len(points)):
        set_score(points,  i)
    print(scores)
    submit(scores)
    

    
