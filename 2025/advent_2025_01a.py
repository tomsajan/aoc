from aocd import data, submit

# data = '''L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82
# '''


if __name__ == '__main__':
    zeros = 0
    current = 50
    for line in data.splitlines():
        dir = line[0]
        num = int(line[1:])
        
        if dir == 'R':
            current += num
        else:
            current -= num
            
        current %= 100
        if current  == 0:
            zeros += 1
    
    print(zeros)
    submit(zeros)
        
        
