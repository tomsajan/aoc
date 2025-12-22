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
    was_zero = False
    for line in data.splitlines():
        dir = line[0]
        num = int(line[1:])
        
        if dir == 'R':
            current += num
        else:
            current -= num

        # if not was_zero and (current > 99 or current <= 0):
        #     print('c range', current)
            # zeros += 1
            
        zeros += abs(current // 100)
        current %= 100
        # was_zero = current == 0
        # print('c modulo', current)

    
    print(zeros)
    submit(zeros)
        
        
