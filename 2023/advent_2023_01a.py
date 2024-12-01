from aocd import data, submit

data = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

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




if __name__ == '__main__':
    soucet = 0
    for line in data.splitlines():
        digits = [znak for znak in line if znak.isdigit()]
        number = int(f'{digits[0]}{digits[-1]}')
        print(number, line)
        soucet += number
        # soucet = soucet + number
        
    print(soucet)
    # submit(soucet)