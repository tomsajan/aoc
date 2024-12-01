from aocd import data, submit

from collections import Counter

# data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''


#data = '''32T3K 765
#T55J5 684
#KK677 28
#KTJJT 220
#QQQJA 483'''


values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5, 
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 1,
        'Q': 11,
        'K': 12,
        'A': 13
        }
FIVE=10
FOUR=9
FULLHOUSE=8
THREE=7
TWO=6
ONE=5
HIGH=4


class Card:
    def __init__(self, letter):
        self.letter = letter

    def __lt__(self, other):
        return values[self.letter] < values[other.letter]
    
    def __lte__(self, other):
        return values[self.letter] <= values[other.letter]

    def __eq__(self, other):
        return values[self.letter] == values[other.letter]


    def __str__(self):
        return str(self.letter) + '_' + str(values[self.letter])
    
    def __repr__(self):
        return self.__str__()

class Hand:
    def __init__(self, hand, bid=0):
       
        best_hand = self.get_best_hand(hand)
        self.hand = tuple(Card(letter) for letter in hand)
        self.raw = hand
        self.bid = bid
        self.type = self.calculate_type(best_hand)
         

    def __str__(self):
        return str(self.hand)+'_'+str(self.get_type())
    
    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        st = self.get_type()
        ot = other.get_type()
        if st < ot:
            return True
        #print('ordering hands', self.hand, self.get_type(), other.hand, other.get_type(),  self.hand < other.hand)
        if st == ot and  self.hand < other.hand:
            return True

        return False

    def __eq__(self, other):
        print('hand qe')
        return self.hand == other.hand

    def __lte__(self, other):
        print('hand lte')
        return self.__lt__(other) or self.__eq__(other)

    def get_type(self):
        return self.type

    def get_best_hand(self, hand):
        if 'J' not in hand:
            return hand
        without_j = hand.replace('J', '')
        c = Counter(without_j)
        if len(c) == 0:
            return hand
        s = sorted(c.items(), key=lambda x: x[1], reverse=True) 
        r  = s[0][0]
        return hand.replace('J', r)


    def calculate_type(self, hand=None):
        if not hand:
            hand = self.raw
        c = Counter(hand)
        #print(self.raw)
        #print(c)
        lc = len(c)
        cv = c.values()
        if lc == 1:
            #print('five')
            return FIVE
        if lc == 2 and 4 in cv:
            #print('four')
            return FOUR
        if lc == 2 and 3 in cv:
            #print('fullhouse')
            return FULLHOUSE
        if lc == 3 and 3 in cv and 1 in cv:
            #print('three')
            return THREE
        if lc == 3 and 2 in cv and 1 in cv:
            #print('two pair')
            return TWO
        if lc == 4 and 2 in cv:
            #print('one pair')
            return ONE
        if lc == 5:
            #print('high card')
            return HIGH
        assert False, 'it should not come to this line'

if __name__ == '__main__':
    hands = []
    for line in data.split('\n'):
        splits = line.split()
        h = Hand(splits[0], int(splits[1]))
        hands.append(h)
        #print(h.get_type())

    #print('unsorted' ,hands)
    hands.sort()
    #print('sorted', hands)

    rank = 0
    points = 0
    for hand in hands:
        rank += 1
        points += rank * hand.bid
    print(points) 
    submit(points)
#    h1 = Hand('32T3K')
#    h2 = Hand('T55J5')
#    h3 = Hand('KK677')
#    h4 = Hand('KTJJT')
#    h5 = Hand('QQQJA')
#    print(h1.hand< h2.hand)
#    print(h2.hand < h1.hand)
#    print(h1.hand[1] < h2.hand[1])
#    print(h2.hand[1] < h1.hand[1])
#
#
#    print(h5 < h2)
#    print(h2 < h5)
#
#    print(h4.hand == h5.hand)
#    print(list(sorted(h4.hand)))
