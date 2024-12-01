from aocd import data, submit

# data = '''two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen'''

# 
# if __name__ == '__main__':
#     elfsum = 0
#     max = 0
#     for n in data.split('\n\n'):
#         elfsum = 0
#         for m in n.split('\n'):
#             elfsum += int(m)
#         if elfsum > max:
#             max = elfsum
#     submit(max)

number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def modify_line(line):
    line = line.replace('eight', '8')
    line = line.replace('two', '2')
    line = line.replace('one', '1')
    line = line.replace('three', '3')
    line = line.replace('four', '4')
    line = line.replace('five', '5')
    line = line.replace('six', '6')
    line = line.replace('nine', '9')
    line = line.replace('seven', '7')
    return line
    

def get_first_number(line):
    while True:
        if line[0].isdigit():
            return line[0]
        for number, word in enumerate(number_words):
            if line.startswith(word):
                return str(number+1)
        line = line[1:]


def get_last_number(line):
    while True:
        if line[-1].isdigit():
            return line[-1]
        for number, word in enumerate(number_words):
            if line.endswith(word):
                return str(number + 1)
        line = line[:-1]


if __name__ == '__main__':
    soucet = 0
    for line in data.splitlines():
        number = int(f'{get_first_number(line)}{get_last_number(line)}')
        # print(number, line)
        soucet += number
        # soucet = soucet + number
        
    print(soucet)
    submit(soucet)