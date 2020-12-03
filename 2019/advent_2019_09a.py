from aocd import data, submit
from lib.intcode import Intcode

if __name__ == '__main__':
    # data = '1102,34915192,34915192,7,4,7,99,0'
    # data = '104,1125899906842624,99'
    # data = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
    ic = Intcode(data)
    ic.set_input(0)
    ic.run()
    print(ic.output)
