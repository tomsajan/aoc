#from aocd import data, submit

data = '''3   4
4   3
2   5
1   3
3   9
3   3
'''

with open('../../aocdownload/input2024-1.txt', 'r') as f:
    data = f.read()

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
    lista = []
    listb = []
    for line in data.splitlines():
        split = line.split()
        lista.append(split[0])
        listb.append(split[1])
        
    lista.sort()
    listb.sort()

    soucet = sum(map(lambda x: abs(int(x[0])-int(x[1])),zip(lista, listb)))


    print(soucet)
    # submit(soucet)
