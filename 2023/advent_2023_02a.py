from aocd import data, submit
from collections import namedtuple


# data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''



Tah = namedtuple('Tah', ['red', 'green', 'blue'], defaults=[0,0,0])

maximal_tah = Tah(red=12, green=13, blue=14)
test_tah = Tah(red=11, green=50, blue=14)
print(test_tah <= maximal_tah)

# print(maximal_tah <= test_tah)
# t = Tah(1,blue=4)

def parse_tah(tahstring):
    red = 0
    green = 0
    blue = 0
    for colorstring in tahstring.split(','):
        count, color = colorstring.split()
        count = int(count.strip())
        color = color.strip()
        
        if color == 'red':
            red = count
        if color == 'blue':
            blue = count
        if color == 'green':
            green = count
            
    return Tah(red=red, green=green, blue=blue)
    

def parse_game(line):
    splits = line.split(':')
    game = int(splits[0].replace('Game ', ''))
    gamedata = [parse_tah(tahstring) for tahstring in splits[1].split(';')]
    
    return game, gamedata



if __name__ == '__main__':

    games  = {}
    for line in data.splitlines():
        game, gamedata = parse_game(line)
        games[game] = gamedata
    
    soucet = sum(  game for game, gamedata in games.items() if all(tah.red <= maximal_tah.red and tah.blue <= maximal_tah.blue and tah.green <= maximal_tah.green for tah in gamedata)   )
    print(soucet)
    submit(soucet)
        